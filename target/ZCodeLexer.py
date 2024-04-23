# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *




def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u017b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\6\2q\n\2\r\2\16")
        buf.write("\2r\3\2\3\2\7\2w\n\2\f\2\16\2z\13\2\5\2|\n\2\3\2\3\2\5")
        buf.write("\2\u0080\n\2\3\2\6\2\u0083\n\2\r\2\16\2\u0084\5\2\u0087")
        buf.write("\n\2\3\3\3\3\3\4\3\4\5\4\u008d\n\4\3\5\3\5\7\5\u0091\n")
        buf.write("\5\f\5\16\5\u0094\13\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u009e\n\6\3\7\3\7\3\b\3\b\3\b\3\b\7\b\u00a6\n\b\f")
        buf.write("\b\16\b\u00a9\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-")
        buf.write("\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\7\62\u0150")
        buf.write("\n\62\f\62\16\62\u0153\13\62\3\63\6\63\u0156\n\63\r\63")
        buf.write("\16\63\u0157\3\63\3\63\3\64\3\64\3\64\3\65\3\65\7\65\u0161")
        buf.write("\n\65\f\65\16\65\u0164\13\65\3\65\3\65\3\65\5\65\u0169")
        buf.write("\n\65\3\65\3\65\3\66\3\66\7\66\u016f\n\66\f\66\16\66\u0172")
        buf.write("\13\66\3\66\3\66\3\66\3\67\3\67\3\67\5\67\u017a\n\67\2")
        buf.write("\28\3\3\5\2\7\4\t\5\13\2\r\6\17\7\21\b\23\t\25\n\27\13")
        buf.write("\31\f\33\r\35\16\37\17!\20#\21%\22\'\23)\24+\25-\26/\27")
        buf.write("\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%")
        buf.write("M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\2\3\2\f")
        buf.write("\4\2GGgg\4\2--//\3\2\62;\6\2\f\f\16\17$$^^\t\2))^^ddh")
        buf.write("hppttvv\4\2\f\f\16\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\n")
        buf.write("\13\16\17\"\"\3\3\f\f\2\u0188\2\3\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\3p\3\2\2\2\5\u0088\3\2")
        buf.write("\2\2\7\u008c\3\2\2\2\t\u008e\3\2\2\2\13\u009d\3\2\2\2")
        buf.write("\r\u009f\3\2\2\2\17\u00a1\3\2\2\2\21\u00ac\3\2\2\2\23")
        buf.write("\u00b1\3\2\2\2\25\u00b7\3\2\2\2\27\u00be\3\2\2\2\31\u00c3")
        buf.write("\3\2\2\2\33\u00ca\3\2\2\2\35\u00d1\3\2\2\2\37\u00d5\3")
        buf.write("\2\2\2!\u00dd\3\2\2\2#\u00e2\3\2\2\2%\u00e6\3\2\2\2\'")
        buf.write("\u00ec\3\2\2\2)\u00ef\3\2\2\2+\u00f5\3\2\2\2-\u00fe\3")
        buf.write("\2\2\2/\u0101\3\2\2\2\61\u0106\3\2\2\2\63\u010b\3\2\2")
        buf.write("\2\65\u0111\3\2\2\2\67\u0115\3\2\2\29\u0119\3\2\2\2;\u011d")
        buf.write("\3\2\2\2=\u0120\3\2\2\2?\u0122\3\2\2\2A\u0124\3\2\2\2")
        buf.write("C\u0126\3\2\2\2E\u0128\3\2\2\2G\u012a\3\2\2\2I\u012c\3")
        buf.write("\2\2\2K\u012f\3\2\2\2M\u0132\3\2\2\2O\u0134\3\2\2\2Q\u0137")
        buf.write("\3\2\2\2S\u0139\3\2\2\2U\u013c\3\2\2\2W\u0140\3\2\2\2")
        buf.write("Y\u0143\3\2\2\2[\u0145\3\2\2\2]\u0147\3\2\2\2_\u0149\3")
        buf.write("\2\2\2a\u014b\3\2\2\2c\u014d\3\2\2\2e\u0155\3\2\2\2g\u015b")
        buf.write("\3\2\2\2i\u015e\3\2\2\2k\u016c\3\2\2\2m\u0179\3\2\2\2")
        buf.write("oq\5\5\3\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2\2s{\3")
        buf.write("\2\2\2tx\7\60\2\2uw\5\5\3\2vu\3\2\2\2wz\3\2\2\2xv\3\2")
        buf.write("\2\2xy\3\2\2\2y|\3\2\2\2zx\3\2\2\2{t\3\2\2\2{|\3\2\2\2")
        buf.write("|\u0086\3\2\2\2}\177\t\2\2\2~\u0080\t\3\2\2\177~\3\2\2")
        buf.write("\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\u0083\5")
        buf.write("\5\3\2\u0082\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086")
        buf.write("}\3\2\2\2\u0086\u0087\3\2\2\2\u0087\4\3\2\2\2\u0088\u0089")
        buf.write("\t\4\2\2\u0089\6\3\2\2\2\u008a\u008d\5\21\t\2\u008b\u008d")
        buf.write("\5\23\n\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\b\3\2\2\2\u008e\u0092\7$\2\2\u008f\u0091\5\13\6\2\u0090")
        buf.write("\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\u0095\3\2\2\2\u0094\u0092\3")
        buf.write("\2\2\2\u0095\u0096\7$\2\2\u0096\u0097\b\5\2\2\u0097\n")
        buf.write("\3\2\2\2\u0098\u009e\n\5\2\2\u0099\u009a\7^\2\2\u009a")
        buf.write("\u009e\t\6\2\2\u009b\u009c\7)\2\2\u009c\u009e\7$\2\2\u009d")
        buf.write("\u0098\3\2\2\2\u009d\u0099\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009e\f\3\2\2\2\u009f\u00a0\7\f\2\2\u00a0\16\3\2\2\2")
        buf.write("\u00a1\u00a2\7%\2\2\u00a2\u00a3\7%\2\2\u00a3\u00a7\3\2")
        buf.write("\2\2\u00a4\u00a6\n\7\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\b\b\3\2")
        buf.write("\u00ab\20\3\2\2\2\u00ac\u00ad\7v\2\2\u00ad\u00ae\7t\2")
        buf.write("\2\u00ae\u00af\7w\2\2\u00af\u00b0\7g\2\2\u00b0\22\3\2")
        buf.write("\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4")
        buf.write("\7n\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6\7g\2\2\u00b6\24")
        buf.write("\3\2\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba")
        buf.write("\7o\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd")
        buf.write("\7t\2\2\u00bd\26\3\2\2\2\u00be\u00bf\7d\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7n\2\2\u00c2\30")
        buf.write("\3\2\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7i\2\2\u00c9\32\3\2\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7w\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf\u00d0\7p\2\2\u00d0\34\3\2\2\2\u00d1\u00d2")
        buf.write("\7x\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7t\2\2\u00d4\36")
        buf.write("\3\2\2\2\u00d5\u00d6\7f\2\2\u00d6\u00d7\7{\2\2\u00d7\u00d8")
        buf.write("\7p\2\2\u00d8\u00d9\7c\2\2\u00d9\u00da\7o\2\2\u00da\u00db")
        buf.write("\7k\2\2\u00db\u00dc\7e\2\2\u00dc \3\2\2\2\u00dd\u00de")
        buf.write("\7h\2\2\u00de\u00df\7w\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7e\2\2\u00e1\"\3\2\2\2\u00e2\u00e3\7h\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7t\2\2\u00e5$\3\2\2\2\u00e6\u00e7")
        buf.write("\7w\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea")
        buf.write("\7k\2\2\u00ea\u00eb\7n\2\2\u00eb&\3\2\2\2\u00ec\u00ed")
        buf.write("\7d\2\2\u00ed\u00ee\7{\2\2\u00ee(\3\2\2\2\u00ef\u00f0")
        buf.write("\7d\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7m\2\2\u00f4*\3\2\2\2\u00f5\u00f6")
        buf.write("\7e\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9")
        buf.write("\7v\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7w\2\2\u00fc\u00fd\7g\2\2\u00fd,\3\2\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7h\2\2\u0100.\3\2\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\u0103\7n\2\2\u0103\u0104\7u\2\2\u0104\u0105")
        buf.write("\7g\2\2\u0105\60\3\2\2\2\u0106\u0107\7g\2\2\u0107\u0108")
        buf.write("\7n\2\2\u0108\u0109\7k\2\2\u0109\u010a\7h\2\2\u010a\62")
        buf.write("\3\2\2\2\u010b\u010c\7d\2\2\u010c\u010d\7g\2\2\u010d\u010e")
        buf.write("\7i\2\2\u010e\u010f\7k\2\2\u010f\u0110\7p\2\2\u0110\64")
        buf.write("\3\2\2\2\u0111\u0112\7g\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7f\2\2\u0114\66\3\2\2\2\u0115\u0116\7p\2\2\u0116\u0117")
        buf.write("\7q\2\2\u0117\u0118\7v\2\2\u01188\3\2\2\2\u0119\u011a")
        buf.write("\7c\2\2\u011a\u011b\7p\2\2\u011b\u011c\7f\2\2\u011c:\3")
        buf.write("\2\2\2\u011d\u011e\7q\2\2\u011e\u011f\7t\2\2\u011f<\3")
        buf.write("\2\2\2\u0120\u0121\7-\2\2\u0121>\3\2\2\2\u0122\u0123\7")
        buf.write("/\2\2\u0123@\3\2\2\2\u0124\u0125\7,\2\2\u0125B\3\2\2\2")
        buf.write("\u0126\u0127\7\61\2\2\u0127D\3\2\2\2\u0128\u0129\7\'\2")
        buf.write("\2\u0129F\3\2\2\2\u012a\u012b\7?\2\2\u012bH\3\2\2\2\u012c")
        buf.write("\u012d\7>\2\2\u012d\u012e\7/\2\2\u012eJ\3\2\2\2\u012f")
        buf.write("\u0130\7#\2\2\u0130\u0131\7?\2\2\u0131L\3\2\2\2\u0132")
        buf.write("\u0133\7>\2\2\u0133N\3\2\2\2\u0134\u0135\7>\2\2\u0135")
        buf.write("\u0136\7?\2\2\u0136P\3\2\2\2\u0137\u0138\7@\2\2\u0138")
        buf.write("R\3\2\2\2\u0139\u013a\7@\2\2\u013a\u013b\7?\2\2\u013b")
        buf.write("T\3\2\2\2\u013c\u013d\7\60\2\2\u013d\u013e\7\60\2\2\u013e")
        buf.write("\u013f\7\60\2\2\u013fV\3\2\2\2\u0140\u0141\7?\2\2\u0141")
        buf.write("\u0142\7?\2\2\u0142X\3\2\2\2\u0143\u0144\7*\2\2\u0144")
        buf.write("Z\3\2\2\2\u0145\u0146\7+\2\2\u0146\\\3\2\2\2\u0147\u0148")
        buf.write("\7]\2\2\u0148^\3\2\2\2\u0149\u014a\7_\2\2\u014a`\3\2\2")
        buf.write("\2\u014b\u014c\7.\2\2\u014cb\3\2\2\2\u014d\u0151\t\b\2")
        buf.write("\2\u014e\u0150\t\t\2\2\u014f\u014e\3\2\2\2\u0150\u0153")
        buf.write("\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152")
        buf.write("d\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0156\t\n\2\2\u0155")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2")
        buf.write("\u0157\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\b")
        buf.write("\63\3\2\u015af\3\2\2\2\u015b\u015c\13\2\2\2\u015c\u015d")
        buf.write("\b\64\4\2\u015dh\3\2\2\2\u015e\u0162\7$\2\2\u015f\u0161")
        buf.write("\5\13\6\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0168\3\2\2\2")
        buf.write("\u0164\u0162\3\2\2\2\u0165\u0166\7\17\2\2\u0166\u0169")
        buf.write("\7\f\2\2\u0167\u0169\t\13\2\2\u0168\u0165\3\2\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\b\65\5")
        buf.write("\2\u016bj\3\2\2\2\u016c\u0170\7$\2\2\u016d\u016f\5\13")
        buf.write("\6\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173\3\2\2\2\u0172")
        buf.write("\u0170\3\2\2\2\u0173\u0174\5m\67\2\u0174\u0175\b\66\6")
        buf.write("\2\u0175l\3\2\2\2\u0176\u0177\7^\2\2\u0177\u017a\n\6\2")
        buf.write("\2\u0178\u017a\7^\2\2\u0179\u0176\3\2\2\2\u0179\u0178")
        buf.write("\3\2\2\2\u017an\3\2\2\2\23\2rx{\177\u0084\u0086\u008c")
        buf.write("\u0092\u009d\u00a7\u0151\u0157\u0162\u0168\u0170\u0179")
        buf.write("\7\3\5\2\b\2\2\3\64\3\3\65\4\3\66\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM_LIT = 1
    BOOL_LIT = 2
    STR_LIT = 3
    NEWLN = 4
    CMT = 5
    TRUE = 6
    FALSE = 7
    NUMBER = 8
    BOOL = 9
    STRING = 10
    RETURN = 11
    VAR = 12
    DYNAMIC = 13
    FUNC = 14
    FOR = 15
    UNTIL = 16
    BY = 17
    BREAK = 18
    CONTINUE = 19
    IF = 20
    ELSE = 21
    ELIF = 22
    BEGIN = 23
    END = 24
    NOT = 25
    AND = 26
    OR = 27
    ADD = 28
    SUB = 29
    MUL = 30
    DIV = 31
    MOD = 32
    RES = 33
    ASG = 34
    UEQL = 35
    LT = 36
    LTE = 37
    GT = 38
    GTE = 39
    CONCAT = 40
    EQL = 41
    CLB = 42
    CRB = 43
    SLB = 44
    SRB = 45
    COMMA = 46
    ID = 47
    WS = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUM_LIT", "BOOL_LIT", "STR_LIT", "NEWLN", "CMT", "TRUE", "FALSE", 
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
            "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
            "BEGIN", "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "RES", "ASG", "UEQL", "LT", "LTE", "GT", "GTE", "CONCAT", 
            "EQL", "CLB", "CRB", "SLB", "SRB", "COMMA", "ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NUM_LIT", "DIGIT", "BOOL_LIT", "STR_LIT", "CHAR", "NEWLN", 
                  "CMT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "RES", 
                  "ASG", "UEQL", "LT", "LTE", "GT", "GTE", "CONCAT", "EQL", 
                  "CLB", "CRB", "SLB", "SRB", "COMMA", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ILL_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.STR_LIT_action 
            actions[50] = self.ERROR_CHAR_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
                    raise UncloseString(self.text[1:-2])
            	elif(self.text[-1] == '\n'):
            		raise UncloseString(self.text[1:-1])
            	else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                y = str(self.text)
                raise IllegalEscape(y[1:])

     


