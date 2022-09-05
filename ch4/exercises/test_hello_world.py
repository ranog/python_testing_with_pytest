from ch4.exercises.hello_world import hello


# 1. Write a test without fixtures that validates that hello() writes the correct content to hello.txt.
def test_hello_world():
    # 4. Comment out the calls to hello() in both tests and re-run. Do they both fail? If not, why not?
    # hello()
    with open('hello.txt') as file:
        text = file.read()
    assert text == 'Hello World!\n'


# 2. Write a second test using fixtures that utilizes a temporary directory and monkeypatch.chdir().
def test_hello_world_using_built_in_fixtures_in_pytest(tmp_path, monkeypatch):
    # 3. Add a print statement to see where the temporary directory is located. Manually check the hello.txt file after
    # a test run. pytest leaves the temporary directories around for a while after test runs to help with debugging.
    print(tmp_path)
    monkeypatch.chdir(tmp_path)
    # 4. Comment out the calls to hello() in both tests and re-run. Do they both fail? If not, why not?
    # hello()
    with open('hello.txt') as file:
        text = file.read()
    assert text == 'Hello World!\n'
