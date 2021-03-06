"""added datetime column 'modified' to members table

Revision ID: 801462becd76
Revises: 68adc2093019
Create Date: 2021-07-10 18:44:56.406475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '801462becd76'
down_revision = '68adc2093019'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('members', 'created')
    # ### end Alembic commands ###
