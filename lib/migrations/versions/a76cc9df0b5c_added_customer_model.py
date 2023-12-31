"""Added Customer model

Revision ID: a76cc9df0b5c
Revises: 987551e03799
Create Date: 2023-09-07 20:02:57.601023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a76cc9df0b5c'
down_revision = '987551e03799'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customers_first_name'), 'customers', ['first_name'], unique=False)
    op.create_index(op.f('ix_customers_last_name'), 'customers', ['last_name'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('product_serialNo', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_product_name'), 'products', ['product_name'], unique=False)
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carts')
    op.drop_index(op.f('ix_products_product_name'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_customers_last_name'), table_name='customers')
    op.drop_index(op.f('ix_customers_first_name'), table_name='customers')
    op.drop_table('customers')
    # ### end Alembic commands ###
