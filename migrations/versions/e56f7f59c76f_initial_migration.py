"""Initial Migration

Revision ID: e56f7f59c76f
Revises: 
Create Date: 2024-03-03 15:43:14.910956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e56f7f59c76f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=50), nullable=False),
    sa.Column('label', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('value')
    )
    op.create_table('payment_type_document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sub_document_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('document_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['document_type_id'], ['document_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('signup_date', sa.DateTime(), nullable=False),
    sa.Column('password_hash', sa.String(length=60), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('subscription_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscription.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('document_template',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('template_text', sa.Text(), nullable=False),
    sa.Column('document_type_id', sa.Integer(), nullable=True),
    sa.Column('sub_document_type_id', sa.Integer(), nullable=True),
    sa.Column('payment_type_document_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['document_type_id'], ['document_type.id'], ),
    sa.ForeignKeyConstraint(['payment_type_document_id'], ['payment_type_document.id'], ),
    sa.ForeignKeyConstraint(['sub_document_type_id'], ['sub_document_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resulting__document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('answers_json', sa.Text(), nullable=False),
    sa.Column('plain_text', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('document_type_id', sa.Integer(), nullable=False),
    sa.Column('document_template_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['document_template_id'], ['document_template.id'], name='fk_document_template_id'),
    sa.ForeignKeyConstraint(['document_type_id'], ['document_type.id'], name='fk_document_type_id'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resulting__document')
    op.drop_table('document_template')
    op.drop_table('user')
    op.drop_table('sub_document_type')
    op.drop_table('subscription')
    op.drop_table('role')
    op.drop_table('questions')
    op.drop_table('payment_type_document')
    op.drop_table('document_type')
    # ### end Alembic commands ###
