"""empty message

Revision ID: 2da343afb05d
Revises: 3bfdd55dcf13
Create Date: 2018-10-15 19:35:29.547233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2da343afb05d'
down_revision = '3bfdd55dcf13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_token', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'user', ['user_token'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'user_token')
    # ### end Alembic commands ###