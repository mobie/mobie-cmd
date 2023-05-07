import jgo.util
import argparse
from importlib.metadata import version
from functools import partial

_picocli_autocomplete = "picocli.AutoComplete"
_mobie_main_class = "org.embl.mobie.cmd.MoBIECmd"
_groupId = "org.embl.mobie"
_artifactId = "mobie-viewer-fiji"
_artifactVersion = version("mobie")


def launch_mobie(main_class, mobie_options):
    return jgo.util.main_from_endpoint(
        argv=mobie_options,
        primary_endpoint=f"{_groupId}:{_artifactId}",
        primary_endpoint_main_class=main_class,
        primary_endpoint_version=_artifactVersion,
    )


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers()
    mobie_project = sub.add_parser("project", add_help=False)
    mobie_project.set_defaults(func=partial(launch_mobie, "org.embl.mobie.cmd.ProjectCmd"))
    mobie_files = sub.add_parser("files", add_help=False)
    mobie_files.set_defaults(func=partial(launch_mobie, "org.embl.mobie.cmd.FilesCmd"))
    mobie_project = sub.add_parser("table", add_help=False)
    mobie_project.set_defaults(func=partial(launch_mobie, "org.embl.mobie.cmd.TableCmd"))
    mobie_files = sub.add_parser("hcs", add_help=False)
    mobie_files.set_defaults(func=partial(launch_mobie, "org.embl.mobie.cmd.HCSCmd"))

    # subparsers don't specify any options, everything is passed to MoBiE
    args, unknown = p.parse_known_args()
    args.func(mobie_options=unknown)
