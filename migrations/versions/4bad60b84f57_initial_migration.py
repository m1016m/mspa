"""Initial migration.

Revision ID: 4bad60b84f57
Revises: 53d60a6960d5
Create Date: 2023-08-08 13:44:14.450527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bad60b84f57'
down_revision = '53d60a6960d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('booking_service_category', sa.String(length=50), nullable=False),
    sa.Column('booking_service', sa.String(length=150), nullable=False),
    sa.Column('booking_datetime', sa.DateTime(), nullable=False),
    sa.Column('is_canceled', sa.Boolean(), server_default='0', nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###
