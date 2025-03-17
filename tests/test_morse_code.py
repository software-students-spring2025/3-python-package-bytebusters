import pytest
import morse_code_converter

class Tests:
	def test_morseEncoderCorrectness(self):
		tests=[["The quick brown fox jumps over the lazy dog.","- .... . / --.- ..- .. -.-. -.- / -... .-. --- .-- -. / ..-. --- -..- / .--- ..- -- .--. ... / --- ...- . .-. / - .... . / .-.. .- --.. -.-- / -.. --- --. .-.-.- "],["Zidane, Yiddish xylophone wonder, vanquished undesirables through simply rendering quisling patterns on neatly maintained long keys, justly instigating heartfelt gratitude for exemplary deeds captured by audio. Adoring brilliant creativity, daring entrepreneurs funded grand halls, inducing judicious kibitzing, lessened measurably night one, perhaps quelled rapidly since tickets usually vanished when xylophonophilics yelled “Zidane!” Zealots yodeled xylophone whimsies, violently upending the standard rigor quieter patrons observed, neatly mutilating long-kept jive interactions, harmony gone, frantically enabling dire change by armfuls.","--.. .. -.. .- -. . --..-- / -.-- .. -.. -.. .. ... .... / -..- -.-- .-.. --- .--. .... --- -. . / .-- --- -. -.. . .-. --..-- / ...- .- -. --.- ..- .. ... .... . -.. / ..- -. -.. . ... .. .-. .- -... .-.. . ... / - .... .-. --- ..- --. .... / ... .. -- .--. .-.. -.-- / .-. . -. -.. . .-. .. -. --. / --.- ..- .. ... .-.. .. -. --. / .--. .- - - . .-. -. ... / --- -. / -. . .- - .-.. -.-- / -- .- .. -. - .- .. -. . -.. / .-.. --- -. --. / -.- . -.-- ... --..-- / .--- ..- ... - .-.. -.-- / .. -. ... - .. --. .- - .. -. --. / .... . .- .-. - ..-. . .-.. - / --. .-. .- - .. - ..- -.. . / ..-. --- .-. / . -..- . -- .--. .-.. .- .-. -.-- / -.. . . -.. ... / -.-. .- .--. - ..- .-. . -.. / -... -.-- / .- ..- -.. .. --- .-.-.- / .- -.. --- .-. .. -. --. / -... .-. .. .-.. .-.. .. .- -. - / -.-. .-. . .- - .. ...- .. - -.-- --..-- / -.. .- .-. .. -. --. / . -. - .-. . .--. .-. . -. . ..- .-. ... / ..-. ..- -. -.. . -.. / --. .-. .- -. -.. / .... .- .-.. .-.. ... --..-- / .. -. -.. ..- -.-. .. -. --. / .--- ..- -.. .. -.-. .. --- ..- ... / -.- .. -... .. - --.. .. -. --. --..-- / .-.. . ... ... . -. . -.. / -- . .- ... ..- .-. .- -... .-.. -.-- / -. .. --. .... - / --- -. . --..-- / .--. . .-. .... .- .--. ... / --.- ..- . .-.. .-.. . -.. / .-. .- .--. .. -.. .-.. -.-- / ... .. -. -.-. . / - .. -.-. -.- . - ... / ..- ... ..- .- .-.. .-.. -.-- / ...- .- -. .. ... .... . -.. / .-- .... . -. / -..- -.-- .-.. --- .--. .... --- -. --- .--. .... .. .-.. .. -.-. ... / -.-- . .-.. .-.. . -.. / .-..-. --.. .. -.. .- -. . -.-.-- .-..-. / --.. . .- .-.. --- - ... / -.-- --- -.. . .-.. . -.. / -..- -.-- .-.. --- .--. .... --- -. . / .-- .... .. -- ... .. . ... --..-- / ...- .. --- .-.. . -. - .-.. -.-- / ..- .--. . -. -.. .. -. --. / - .... . / ... - .- -. -.. .- .-. -.. / .-. .. --. --- .-. / --.- ..- .. . - . .-. / .--. .- - .-. --- -. ... / --- -... ... . .-. ...- . -.. --..-- / -. . .- - .-.. -.-- / -- ..- - .. .-.. .- - .. -. --. / .-.. --- -. --. -....- -.- . .--. - / .--- .. ...- . / .. -. - . .-. .- -.-. - .. --- -. ... --..-- / .... .- .-. -- --- -. -.-- / --. --- -. . --..-- / ..-. .-. .- -. - .. -.-. .- .-.. .-.. -.-- / . -. .- -... .-.. .. -. --. / -.. .. .-. . / -.-. .... .- -. --. . / -... -.-- / .- .-. -- ..-. ..- .-.. ... .-.-.- "]]
		for test in tests:
			assert(morse_code_converter.toMorse(test[0])==test[1])
	def test_morseEncoderError(self,capsys):
		tests=[["Съешь ещё этих мягких французских булок, да выпей же чаю","ERROR: UNSUPPORTED CHARACTERS"]]
		for test in tests:
			with pytest.raises(Exception):
				morse_code_converter.toMorse(test[0])==test[1]
	def test_morseEncoderEmpty(self,capsys):
		with pytest.raises(Exception):
			morse_code_converter.toMorse("")
