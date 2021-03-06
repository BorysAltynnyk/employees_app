"""empty message

Revision ID: 5596c73d7e02
Revises: 327308c951ed
Create Date: 2020-12-08 11:10:01.418453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5596c73d7e02'
down_revision = '327308c951ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('department', 'avr_salary')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('department', sa.Column('avr_salary', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
