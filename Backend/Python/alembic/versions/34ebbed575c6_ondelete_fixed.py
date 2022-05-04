"""ondelete fixed

Revision ID: 34ebbed575c6
Revises: 467ea8a06897
Create Date: 2022-04-28 20:48:19.220061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34ebbed575c6'
down_revision = '467ea8a06897'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('association_account_id_fkey', 'association', type_='foreignkey')
    op.drop_constraint('association_user_id_fkey', 'association', type_='foreignkey')
    op.create_foreign_key(None, 'association', 'accounts', ['account_id'], ['ID_Acc'], ondelete='CASCADE')
    op.create_foreign_key(None, 'association', 'users', ['user_id'], ['ID_Usr'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'association', type_='foreignkey')
    op.drop_constraint(None, 'association', type_='foreignkey')
    op.create_foreign_key('association_user_id_fkey', 'association', 'users', ['user_id'], ['ID_Usr'])
    op.create_foreign_key('association_account_id_fkey', 'association', 'accounts', ['account_id'], ['ID_Acc'])
    # ### end Alembic commands ###