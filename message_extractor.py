from html.parser import HTMLParser
from html.entities import name2codepoint


def parse_messages(filepath):
    print("reading file...", filepath)
    with open(filepath) as f:
        text = f.read()
    parser = MyHTMLParser()
    parser.feed(text)


class MyHTMLParser(HTMLParser):
    set_user = False
    current_user = ""
    last_user = ""
    set_message = False

    def handle_starttag(self, tag, attrs):
        # print("messages:", messages)
        # print("Start tag:", tag)
        # for (key, val) in attrs:
        #     print("     attr:", key, val)
        if tag == "span" and len(attrs) > 0 and attrs[0][0] == "class" and attrs[0][1] == "user":
            # print("setting user tag!")
            self.set_user = True
        elif tag == "p":
            self.set_message = True
            # print("message!")

            # def handle_endtag(self, tag):
            # print("End tag  :", tag)

    def handle_data(self, data):
        if self.set_user:
            self.set_user = False
            self.last_user = self.current_user
            self.current_user = data
            # print("current user:", data)
        elif self.set_message:
            if self.current_user == name:
                if self.last_user == name:  # had multiple messages from same person
                    messages[-1] += " " + data
                else:
                    messages.append(data)
            self.set_message = False
            # print("Data     :", data)

    # def handle_comment(self, data):
    #     print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        # print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
            # print("Num ent  :", c)

            # def handle_decl(self, data):
            #     print("Decl     :", data)


if __name__ == "__main__":
    name = "Muthu Chidambaram"
    # input_file = "data/chandan/messages_readable.html"
    input_file = "data/chandan/html/messages.htm"
    output_file = "data/chandan/messages_out.html"
    messages = []
    parse_messages(input_file)
    print('writing file...')
    with open(output_file, 'w') as f:
        for line in messages:
            f.write(line + '\n')
