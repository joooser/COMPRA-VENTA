"""change name of table to plural questions

Revision ID: 18d969ad0345
Revises: 59ebbfa88461
Create Date: 2024-01-06 17:33:49.649466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18d969ad0345'
down_revision = '59ebbfa88461'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('question')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('text', sa.VARCHAR(length=255), nullable=False),
    sa.Column('category', sa.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('questions')
    # ### end Alembic commands ###
