"""empty message

Revision ID: 3ef85d686bd1
Revises: 8b96c89f93b5
Create Date: 2018-10-16 20:06:21.896065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ef85d686bd1'
down_revision = '8b96c89f93b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinemas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('district', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('hallnum', sa.Integer(), nullable=True),
    sa.Column('servicecharge', sa.Integer(), nullable=True),
    sa.Column('astrict', sa.Integer(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinemas')
    # ### end Alembic commands ###