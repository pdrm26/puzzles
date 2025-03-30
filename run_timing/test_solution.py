from solution import run_timing


class TestRunTiming:

    def test_valid_input(self, monkeypatch, capsys):
        responses = ['10.5', '20', '30.2', '']
        monkeypatch.setattr("builtins.input", lambda prompt: responses.pop(0))
        run_timing()
        captured = capsys.readouterr()
        assert "Average of 20.23, over 3 runs" in captured.out

    def test_empty_input(self, monkeypatch, capsys):
        responses = ["  "]
        monkeypatch.setattr('builtins.input', lambda prompt: responses.pop(0))
        run_timing()
        captured = capsys.readouterr()
        assert "No run times were entered." in captured.out

    def test_mixed_valid_invalid_input(self, monkeypatch, capsys):
        responses = ['10', '2.2', 'abc', '']
        monkeypatch.setattr('builtins.input', lambda prompt: responses.pop(0))
        run_timing()
        captured = capsys.readouterr()
        assert "Invalid input: could not convert string to float: 'abc'" in captured.out
        assert "Average of 6.10, over 2 runs" in captured.out

    def test_negative_input(self, monkeypatch, capsys):
        responses = ['-10', '']
        monkeypatch.setattr("builtins.input", lambda prompt: responses.pop(0))
        run_timing()
        captured = capsys.readouterr()
        assert "Invalid input: Run time must be over Zero" in captured.out
        assert "No run times were entered." in captured.out

    def test_zero_input(self, monkeypatch, capsys):
        responses = ['0', '']
        monkeypatch.setattr('builtins.input', lambda prompt: responses.pop(0))
        run_timing()
        captured = capsys.readouterr()
        assert "Invalid input: Run time must be over Zero" in captured.out
        assert "No run times were entered." in captured.out