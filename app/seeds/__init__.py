from flask.cli import AppGroup
from .users import seed_users, undo_users
from .designs import seed_designs, undo_designs
from .fonts import seed_fonts, undo_seed_fonts
from .colors import seed_colors, undo_seed_colors
# from .logo import seed_logo, undo_seed_logo
from .shapes import seed_shapes, undo_seed_shapes
from .brands import seed_brands, undo_brands
from .templates import seed_templates, undo_seed_templates

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    # Add other seed functions here
    seed_shapes()
    seed_templates()
    seed_designs()

    seed_fonts()
    seed_colors()
    seed_brands()

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
    undo_seed_shapes()
    undo_seed_templates()
    undo_designs()
    undo_seed_fonts()
    undo_seed_colors()
    undo_brands()
