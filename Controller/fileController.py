import os
from flask import Blueprint, render_template, abort, send_file
from lagom.experimental.integrations.flask import FlaskBlueprintIntegration
from container import container


def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree

file_controller = Blueprint('file_controller', __name__)
file_controller_with_deps = FlaskBlueprintIntegration(file_controller, container)


@file_controller_with_deps.route('/', defaults={'req_path': ''})
@file_controller_with_deps.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = os.getcwd()+"/blacklists"

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)
    # path traversal path
    abs_path_to_check = os.path.normpath(abs_path)
    if abs_path_to_check.startswith(os.path.normpath(os.path.abspath(BASE_DIR)+os.sep)):
        # Return 404 if path doesn't exist
        if not os.path.exists(abs_path):
            return abort(404)

        # Check if path is a file and serve
        if os.path.isfile(abs_path):
            return send_file(abs_path)

        # Show directory contents
        files = os.listdir(abs_path)
        return render_template('dirtree.html', files=files)
    else:
        return abort(404)