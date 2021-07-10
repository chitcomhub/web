"""changed column name from created to modified

Revision ID: 09cd9fd02e5c
Revises: 801462becd76
Create Date: 2021-07-10 18:53:29.107199

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '09cd9fd02e5c'
down_revision = '801462becd76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('modified', sa.DateTime(), nullable=True))
    op.drop_column('members', 'created')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('members', 'modified')
    # ### end Alembic commands ###