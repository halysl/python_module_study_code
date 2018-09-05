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


def run(cmd, filter_=False, ssh=None):
    """
    run a command
    """
    logger.info(">>>>>>>>>>>>>>>> cmd: {} <<<<<<<<<<<<<<<<<<".format(cmd))
    result = {}
    out_msg = ''
    try:
        if ssh:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            stdin.close()
            stdout.flush()
            out_msg = stdout.read()
            err_msg = stderr.read()
            exit_code = 0
        else:
            p = subprocess.Popen(cmd, shell=True, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out_msg = p.stdout.read()
            err_msg = p.stderr.read()
            exit_code = p.wait()

        if filter_:
            out_list = out_msg.splitlines()
            if "Exit Code" in out_list[-1]:
                out_msg = "\n".join(out_list[:-1])
        result["stdout"] = out_msg
        result["stderr"] = err_msg
        result["exit_code"] = exit_code
        logger.info("cmd output:\n" + out_msg)
        if err_msg:
            logger.exception("cmd error msg:\n" + err_msg)
        return result
    except Exception as e:
        logger.exception("exception at run {}: {}".format(cmd, e))
        result["stdout"] = ""
        result["stderr"] = e
        result["exit_code"] = 1
        return result


def run_cmd(cmd, filter_=False, ssh=None):
    result = run(cmd=cmd, filter_=filter_, ssh=ssh)
    if result["exit_code"] != 0:
        msg = result["stderr"].strip() if result["stderr"] else result["stdout"].strip()
        raise Exception(msg)
    else:
        return result["stdout"]


base_path = os.path.dirname(os.path.abspath(__file__))

log_dir = os.path.join(base_path, 'test_tar_args')
target = os.path.join(base_path, 'x.tar.gz')
cmd = 'find {} -mtime -10 -print0 | xargs -0 tar czvf {}'.format(log_dir, target)

# --warning=no-file-changed --absolute-names
info = "collect grid files which changed in 10 days"
try:
    run_cmd(cmd)
    print('green', info)
except:
    print("red {}, the command is: {}".format(info, cmd))


