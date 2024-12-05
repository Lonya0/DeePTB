from typing import Dict, List, Optional, Any
import ase.io as io
from pathlib import Path
from dptb.utils.tools import get_neighbours
import os


def bond(
        struct: str,
        accuracy: float,
        cutoff: float,
        log_level: int,
        log_path: Optional[str],
        **kwargs
) -> str:
    """Bond distance analysis.

    Parameters
    ----------
    struct : str
        The structure input by 'bond' subcommand.
    accuracy : float
        The accuracy to judge whether two bond are the same. Input by 'bond -acc
        --accuracy' subcommand. (Default value is settled by main_parser at 1e-3)
    cutoff : float
        The cutoff radius of bond search. Input by 'bond -c --cutoff' subcommand.
        (Default value is settled by main_parser at 6.0)
    log_level : int, default=logging.INFO
        Logging level.
    log_path : Optional[str], default=None
        Path to log file.
    **kwargs
        Additional keyword arguments (unused in this implementation).

    Returns
    -------
    str
        Returns bond str after print it out.

    """
    atom = io.read(struct)
    nb = get_neighbours(atom=atom, cutoff=cutoff, thr=accuracy)

    count = 0
    out = ""
    for k,v in nb.items():
        out += "%10s" % k
        if len(v)>count:
            count = len(v)
        if len(v) != 0:
             for i in v:
                 out += '%10.2f'%i
        out += "\n"

    out = "%10s"*(count+1) % tuple(["Bond Type"] + list(range(1,count+1))) + \
        "\n"+ "--"*6*(count+1)+"\n"+ out

    print(out)

    return out
