import os
import logging
import subprocess

def get_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        )
    _logger = logging.getLogger("collect-log")
    _logger.setLevel(logging.INFO)
    return _logger


logger = get_logger()


def run(cmd):
    result = {}

    p = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out_msg = p.stdout.read()
    err_msg = p.stderr.read()
    exit_code = p.wait()

    result["stdout"] = out_msg
    result["stderr"] = err_msg
    result["exit_code"] = exit_code
    logger.info("cmd output:\n" + out_msg)

    if err_msg:
        logger.exception("cmd error msg:\n" + err_msg)
    return result


base_path = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(base_path, 'test_tar_args')
target = os.path.join(base_path, 'x.tar.gz')
cmd = 'find {} -mtime -10 -print0 | xargs -0 tar czvf {}'.format(log_dir, target)

run(cmd)


