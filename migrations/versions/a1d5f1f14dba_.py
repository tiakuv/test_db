"""empty message

Revision ID: a1d5f1f14dba
Revises: 
Create Date: 2020-06-03 08:39:58.774692

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'a1d5f1f14dba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.Column('icon', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('icon'),
    sa.UniqueConstraint('name')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('picture', sa.String(length=50), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('schedule', sqlite.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('picture')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.String(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals_teachers',
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], )
    )
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    op.drop_table('goals_teachers')
    op.drop_table('bookings')
    op.drop_table('teachers')
    op.drop_table('goals')
    op.drop_table('clients')
    # ### end Alembic commands ###
