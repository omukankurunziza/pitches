"""nine Migration

Revision ID: c79549828597
Revises: 11c3f9787c5b
Create Date: 2019-03-04 14:39:02.699954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c79549828597'
down_revision = '11c3f9787c5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('author', sa.String(length=255), nullable=True))
    op.add_column('pitches', sa.Column('pitch_content', sa.String(length=255), nullable=True))
    op.drop_column('pitches', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'pitch_content')
    op.drop_column('pitches', 'author')
    # ### end Alembic commands ###
