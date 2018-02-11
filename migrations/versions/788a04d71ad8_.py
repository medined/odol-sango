"""empty message

Revision ID: 788a04d71ad8
Revises: 
Create Date: 2018-02-11 14:02:26.662859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '788a04d71ad8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blood_sugar_month',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('month', sa.Integer(), nullable=True),
    sa.Column('morning1', sa.Integer(), nullable=True),
    sa.Column('evening1', sa.Integer(), nullable=True),
    sa.Column('morning2', sa.Integer(), nullable=True),
    sa.Column('evening2', sa.Integer(), nullable=True),
    sa.Column('morning3', sa.Integer(), nullable=True),
    sa.Column('evening3', sa.Integer(), nullable=True),
    sa.Column('morning4', sa.Integer(), nullable=True),
    sa.Column('evening4', sa.Integer(), nullable=True),
    sa.Column('morning5', sa.Integer(), nullable=True),
    sa.Column('evening5', sa.Integer(), nullable=True),
    sa.Column('morning6', sa.Integer(), nullable=True),
    sa.Column('evening6', sa.Integer(), nullable=True),
    sa.Column('morning7', sa.Integer(), nullable=True),
    sa.Column('evening7', sa.Integer(), nullable=True),
    sa.Column('morning8', sa.Integer(), nullable=True),
    sa.Column('evening8', sa.Integer(), nullable=True),
    sa.Column('morning9', sa.Integer(), nullable=True),
    sa.Column('evening9', sa.Integer(), nullable=True),
    sa.Column('morning10', sa.Integer(), nullable=True),
    sa.Column('evening10', sa.Integer(), nullable=True),
    sa.Column('morning11', sa.Integer(), nullable=True),
    sa.Column('evening11', sa.Integer(), nullable=True),
    sa.Column('morning12', sa.Integer(), nullable=True),
    sa.Column('evening12', sa.Integer(), nullable=True),
    sa.Column('morning13', sa.Integer(), nullable=True),
    sa.Column('evening13', sa.Integer(), nullable=True),
    sa.Column('morning14', sa.Integer(), nullable=True),
    sa.Column('evening14', sa.Integer(), nullable=True),
    sa.Column('morning15', sa.Integer(), nullable=True),
    sa.Column('evening15', sa.Integer(), nullable=True),
    sa.Column('morning16', sa.Integer(), nullable=True),
    sa.Column('evening16', sa.Integer(), nullable=True),
    sa.Column('morning17', sa.Integer(), nullable=True),
    sa.Column('evening17', sa.Integer(), nullable=True),
    sa.Column('morning18', sa.Integer(), nullable=True),
    sa.Column('evening18', sa.Integer(), nullable=True),
    sa.Column('morning19', sa.Integer(), nullable=True),
    sa.Column('evening19', sa.Integer(), nullable=True),
    sa.Column('morning20', sa.Integer(), nullable=True),
    sa.Column('evening20', sa.Integer(), nullable=True),
    sa.Column('morning21', sa.Integer(), nullable=True),
    sa.Column('evening21', sa.Integer(), nullable=True),
    sa.Column('morning22', sa.Integer(), nullable=True),
    sa.Column('evening22', sa.Integer(), nullable=True),
    sa.Column('morning23', sa.Integer(), nullable=True),
    sa.Column('evening23', sa.Integer(), nullable=True),
    sa.Column('morning24', sa.Integer(), nullable=True),
    sa.Column('evening24', sa.Integer(), nullable=True),
    sa.Column('morning25', sa.Integer(), nullable=True),
    sa.Column('evening25', sa.Integer(), nullable=True),
    sa.Column('morning26', sa.Integer(), nullable=True),
    sa.Column('evening26', sa.Integer(), nullable=True),
    sa.Column('morning27', sa.Integer(), nullable=True),
    sa.Column('evening27', sa.Integer(), nullable=True),
    sa.Column('morning28', sa.Integer(), nullable=True),
    sa.Column('evening28', sa.Integer(), nullable=True),
    sa.Column('morning29', sa.Integer(), nullable=True),
    sa.Column('evening29', sa.Integer(), nullable=True),
    sa.Column('morning30', sa.Integer(), nullable=True),
    sa.Column('evening30', sa.Integer(), nullable=True),
    sa.Column('morning31', sa.Integer(), nullable=True),
    sa.Column('evening31', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blood_sugar_month_uuid'), 'blood_sugar_month', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blood_sugar_month_uuid'), table_name='blood_sugar_month')
    op.drop_table('blood_sugar_month')
    # ### end Alembic commands ###