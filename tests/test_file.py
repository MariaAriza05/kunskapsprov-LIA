def test_file_content():
    file_path = "hello.txt"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        
#kontorllerar innehållet i filen
    assert content == "Hello World!" 

#Ser till att filen inte är tom
    assert len(content) > 0 
