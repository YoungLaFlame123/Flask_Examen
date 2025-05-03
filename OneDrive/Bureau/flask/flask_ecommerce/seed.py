# from app.models import db, Product
# from main import app

# with app.app_context():
#     db.drop_all()  # ⚠️ Supprime toutes les tables (utile en dev uniquement)
#     db.create_all()

#     # Ajoute quelques produits
#     produit1 = Product(name="T-shirt blanc", description="Un t-shirt confortable", price=19.99, image_url="https://via.placeholder.com/150")
#     produit2 = Product(name="Jean bleu", description="Jean tendance", price=49.99, image_url="https://via.placeholder.com/150")
#     produit3 = Product(name="Basket Nike", description="Chaussures stylées", price=89.99, image_url="https://via.placeholder.com/150")

#     db.session.add_all([produit1, produit2, produit3])
#     db.session.commit()

#     print("✅ Produits insérés avec succès !")
