"""empty message

Revision ID: c61c62964001
Revises: 2da343afb05d
Create Date: 2018-10-16 00:14:07.202283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c61c62964001'
down_revision = '2da343afb05d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('permission', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'permission')
    # ### end Alembic commands ###