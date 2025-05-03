from flask import render_template, session, redirect, url_for, flash 
from app.forms.product_form import ProductForm
from app.models import Product,db
    
def register_routes(app):
    @app.route('/')
    def index():
        products = Product.query.all()
        return render_template('index.html', products=products)

    @app.route('/ajouter_panier/<int:product_id>')
    def ajouter_panier(product_id):
        panier = session.get('panier', {})
        panier[str(product_id)] = panier.get(str(product_id), 0) + 1
        session['panier'] = panier
        return redirect(url_for('index'))
    
    # Route détail produit
    @app.route('/produit/<int:product_id>')
    def produit_detail(product_id):
        product = Product.query.get_or_404(product_id)  # Récupère le produit ou renvoie une erreur 404 si non trouvé
        return render_template('produit_detail.html', product=product)

    @app.route('/panier')
    def panier():
        panier = session.get('panier', {})
        produits = []
        total = 0

        for pid, qty in panier.items():
            produit = Product.query.get(int(pid))
            if produit:
                produit.qty = qty
                produit.total = produit.price * qty
                total += produit.total
                produits.append(produit)

        return render_template('panier.html', produits=produits, total=total)
    @app.route('/ajouter_produit', methods=['GET', 'POST'])
    def ajouter_produit():
        form = ProductForm()

        if form.validate_on_submit():  # Si le formulaire est valide et soumis
            # Création d'un nouveau produit
            new_product = Product(
                name=form.name.data,
                description=form.description.data,
                price=form.price.data,
                image_url=form.image_url.data
            )
        
            db.session.add(new_product)
            db.session.commit()
            flash('Produit créé avec succès!', 'success')
            return redirect(url_for('index'))  # Redirige vers la page d'accueil après la création

        return render_template('ajouter_produit.html', form=form)
    @app.route('/supprimer_produit/<int:product_id>', methods=['POST'])
    def supprimer_produit(product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        flash("Produit supprimé avec succès !", "success")
        return redirect(url_for('index'))
    @app.route('/modifier_produit/<int:product_id>', methods=['GET', 'POST'])
    def modifier_produit(product_id):
        product = Product.query.get_or_404(product_id)
        form = ProductForm(obj=product)  # Préremplit le formulaire avec les données du produit

        if form.validate_on_submit():
        # Mise à jour des champs
            product.name = form.name.data
            product.description = form.description.data
            product.price = form.price.data
            product.image_url = form.image_url.data

            db.session.commit()
            flash("Produit modifié avec succès !", "success")
            return redirect(url_for('index'))

        return render_template('modifier_produit.html', form=form, product=product)

