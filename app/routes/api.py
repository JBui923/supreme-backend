from flask import Blueprint, request, jsonify
import jwt

from ..models.models import db, User, Product, Transaction, Review
from ..config import Configuration


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/users", methods=["POST"])
def signup_user():
    print(request.get_json)
    data = request.json
    user = User(first_name=data["firstName"], last_name=data["lastName"], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
    return {'access_token': access_token.decode('UTF-8'), 'user': user.to_dict()}
    



@bp.route("/all")
def get_all_products():
    fetchedProducts = Product.query.all()
    products = [product.to_dict() for product in fetchedProducts]
    return {"products": products}


@bp.route("/transactions", methods=["POST"])
def create_transaction():
    data = request.json
    try:
        transaction = Transaction(products=data["products"], user_id=data["userId"], total=data["total"])
        db.session.add(transaction)
        db.session.commit()
        return jsonify({"transaction": "transaction created"})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/transactions/<int:userId>")
def get_transaction(userId):
    fetchedTrans = Transaction.query.filter(Transaction.user_id == userId).all()
    transactions = [transaction.to_dict() for transaction in fetchedTrans] 
    return jsonify({"transactions": transactions})


@bp.route("/reviews/<int:productId>", methods=["POST"])
def create_reviews(productId):
    data = request.json
    try:
        review = Review(user_id=data["userId"], first_name=data["firstName"], last_name=data["lastName"], product_id=data["productId"], review_body=data["reviewBody"])
        db.session.add(review)
        db.session.commit()
        return jsonify({"review": review.to_dict()})
    except AssertionError as message:
        print(str(message))
        return jsonify({"error": str(message)}), 400


@bp.route("/reviews/<int:productId>")
def get_reviews(productId):
    fetchedReviews = Review.query.filter(Review.product_id == productId).all()
    reviews = [review.to_dict() for review in fetchedReviews]
    return {"reviews": reviews}