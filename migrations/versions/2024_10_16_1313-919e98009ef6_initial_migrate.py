"""Initial Migrate

Revision ID: 919e98009ef6
Revises: 
Create Date: 2024-10-16 13:13:10.319800

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "919e98009ef6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "voceovers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("text", sa.String(length=256), nullable=False),
        sa.Column("voiceover_path", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("voiceover_path"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("voceovers")
    # ### end Alembic commands ###
