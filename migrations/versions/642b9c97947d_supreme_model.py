"""supreme model

Revision ID: 642b9c97947d
Revises: 
Create Date: 2020-07-27 04:35:01.058474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642b9c97947d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=1000), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('imgurl', sa.String(), nullable=False),
    sa.Column('color', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=False),
    sa.Column('new', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('productsizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('small', sa.Boolean(), nullable=True),
    sa.Column('medium', sa.Boolean(), nullable=True),
    sa.Column('large', sa.Boolean(), nullable=True),
    sa.Column('xlarge', sa.Boolean(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('review_body', sa.String(length=1000), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('products', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('reviews')
    op.drop_table('productsizes')
    op.drop_table('users')
    op.drop_table('products')
    # ### end Alembic commands ###
