"""empty message

Revision ID: 73edf1509d6b
Revises: d6a7a6a599f7
Create Date: 2018-10-10 01:09:38.061168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73edf1509d6b'
down_revision = 'd6a7a6a599f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('usermovie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=16), nullable=True),
    sa.Column('age', sa.String(length=16), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('collection',
    sa.Column('usermovie_id', sa.Integer(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['usermovie_id'], ['usermovie.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collection')
    op.drop_table('usermovie')
    op.drop_table('movie')
    # ### end Alembic commands ###