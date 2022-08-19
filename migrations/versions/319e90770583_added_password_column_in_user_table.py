"""Added password column in user table

Revision ID: 319e90770583
Revises: 41b596e265bc
Create Date: 2022-08-15 18:28:50.533688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '319e90770583'
down_revision = '41b596e265bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
