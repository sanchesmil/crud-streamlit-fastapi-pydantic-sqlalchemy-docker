from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductUpdate
from models import ProductModel

# Arquivo responsável por fazer as funções de CRUD do SQLALCHEMY 

# GET ALL (SELECT * FROM)
def get_products(db: Session):
    """ Função que retorna todos os produtos """
    return db.query(ProductModel).all();

# GET WHERE ID = X
def get_product(product_id: int, db: Session):
    """ Função que retorna um produto específico """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# INSERT INTO (CREATE)
def create_product(product: ProductCreate, db: Session):
    """ Função que cria um novo produto """
    # transformar instância do Pydantic em instância do ORM Alchemy (** = desempacotar)
    db_product = ProductModel(**product.model_dump())

    # adicionar na tabela
    db.add(db_product)

    # commitar na tabela
    db.commit()

    # fazer o refresh buscando o produto recem criado
    db.refresh(db_product)

    # retornar o item criado
    return db_product

# UPDATE WHERE ID = X
def update_product(product: ProductUpdate, product_id: int, db: Session):
    """ Função que atualiza um produto """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.categoria is not None:
        db_product.categoria = product.categoria

    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    # commitar na tabela
    db.commit()

    # fazer o refresh buscando o produto recem criado
    db.refresh(db_product)

    # retornar o item criado
    return db_product


# DELETE WHERE ID = X
def delete_product(product_id: int, db: Session):
    """ Função que remove um produto específico """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product
    