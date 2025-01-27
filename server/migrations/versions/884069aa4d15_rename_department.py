"""rename department

Revision ID: 884069aa4d15
Revises: 3d99ddbf6291
Create Date: 2024-01-04 20:05:21.364764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '884069aa4d15'
down_revision = '3d99ddbf6291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
