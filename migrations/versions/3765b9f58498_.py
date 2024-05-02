"""empty message

Revision ID: 3765b9f58498
Revises: 95fb59705926
Create Date: 2024-04-17 13:24:02.854667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3765b9f58498'
down_revision = '95fb59705926'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
