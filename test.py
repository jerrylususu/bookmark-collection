import unittest
from dump_bookmark_md_to_json import parse_bookmark_line

# python -m unittest test.py -v

class TestBookmarkParser(unittest.TestCase):
    def test_with_note_and_tags(self):
        line = '- [title](http://url.com) 备注内容 #tag1#tag2'
        result = parse_bookmark_line(line)
        print(f"\n测试用例1 输入: {line}")
        print("解析结果:", result)
        self.assertEqual(result['note'], '备注内容')
        self.assertListEqual(result['tags'], ['tag1', 'tag2'])

    def test_no_note_with_tags(self):
        line = '- [title](http://url.com) #tag1#tag2'
        result = parse_bookmark_line(line)
        print(f"\n测试用例2 输入: {line}")
        print("解析结果:", result)
        self.assertEqual(result['note'], '')
        self.assertListEqual(result['tags'], ['tag1', 'tag2'])

    def test_with_note_no_tags(self):
        line = '- [title](http://url.com) 只有备注'
        result = parse_bookmark_line(line)
        print(f"\n测试用例3 输入: {line}")
        print("解析结果:", result)
        self.assertEqual(result['note'], '只有备注')
        self.assertListEqual(result['tags'], [])

    def test_minimal_format(self):
        line = '- [title](http://url.com)'
        result = parse_bookmark_line(line)
        print(f"\n测试用例4 输入: {line}")
        print("解析结果:", result)
        self.assertEqual(result['note'], '')
        self.assertListEqual(result['tags'], [])

    def test_multiple_spaces(self):
        line = '- [title](url)   多个空格测试   #tag1#tag2  '
        result = parse_bookmark_line(line)
        print(f"\n测试用例5 输入: {line}")
        print("解析结果:", result)
        self.assertEqual(result['note'], '多个空格测试')
        self.assertListEqual(result['tags'], ['tag1', 'tag2'])

if __name__ == '__main__':
    unittest.main(verbosity=2) 