from alembic import op
import sqlalchemy as sa
from app.core.security import hash_password

revision = "NUEVO_ID"
down_revision = "8a69b8141e5c"
branch_labels = None
depends_on = None


def upgrade():
    users_table = sa.table(
        "users",
        sa.column("username", sa.String),
        sa.column("hashed_password", sa.String),
    )

    op.bulk_insert(
        users_table,
        [
            {
                "username": "admin",
                "hashed_password": hash_password("admin123"),
            }
        ],
    )


def downgrade():
    op.execute("DELETE FROM users WHERE username='admin'")
