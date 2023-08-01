"""empty message

Revision ID: 9625a9f672dc
Revises: 24b22d88be08
Create Date: 2023-07-31 01:48:33.799078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9625a9f672dc'
down_revision = '24b22d88be08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student_field',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('student_id', 'field_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_field')
    op.drop_table('field')
    # ### end Alembic commands ###
