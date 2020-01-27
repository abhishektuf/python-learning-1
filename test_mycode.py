import subprocess

def test_system_command():
    """Test the exit code of a system command"""
    command = 'ping google.com'
    result = subprocess.run(command.split(' '), stdout=subprocess.PIPE)
    print(result.stdout)
    assert result.returncode == 0