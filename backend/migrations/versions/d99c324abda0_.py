"""empty message

Revision ID: d99c324abda0
Revises: fb8fc8718d6c
Create Date: 2025-03-12 21:21:14.621730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd99c324abda0'
down_revision: Union[str, None] = 'fb8fc8718d6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vacancies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('vacancy_id', sa.String(), nullable=False),
    sa.Column('vacancy_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('archived', sa.Boolean(), nullable=False),
    sa.Column('company_name', sa.String(), nullable=False),
    sa.Column('company_logo', sa.String(), nullable=False),
    sa.Column('company_address', sa.String(), nullable=False),
    sa.Column('vacancy_created_at', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancies')
    # ### end Alembic commands ###
