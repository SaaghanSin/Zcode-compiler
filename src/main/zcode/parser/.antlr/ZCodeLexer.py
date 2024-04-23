# Generated from c:\PPL\232-Now\BTL\BTL3\assignment3-initial\src\main\zcode\parser\ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0181\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3%")
        buf.write("\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\7+\u0117")
        buf.write("\n+\f+\16+\u011a\13+\3,\3,\3,\3,\3,\3,\7,\u0122\n,\f,")
        buf.write("\16,\u0125\13,\3,\3,\3,\3-\3-\5-\u012c\n-\3-\5-\u012f")
        buf.write("\n-\3.\6.\u0132\n.\r.\16.\u0133\3/\3/\7/\u0138\n/\f/\16")
        buf.write("/\u013b\13/\3\60\3\60\5\60\u013f\n\60\3\60\6\60\u0142")
        buf.write("\n\60\r\60\16\60\u0143\3\61\3\61\3\62\3\62\3\62\3\62\7")
        buf.write("\62\u014c\n\62\f\62\16\62\u014f\13\62\3\62\3\62\3\63\6")
        buf.write("\63\u0154\n\63\r\63\16\63\u0155\3\63\3\63\3\64\3\64\3")
        buf.write("\64\3\65\3\65\7\65\u015f\n\65\f\65\16\65\u0162\13\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\7\66\u0169\n\66\f\66\16\66\u016c")
        buf.write("\13\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u0176")
        buf.write("\n\67\38\38\38\58\u017b\n8\39\39\39\59\u0180\n9\2\2:\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[\2]\2_\2a/c\60e\61g\62i\63k\64m\2o\2q\2\3\2\21")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2$$\6\2\f\f\16\17$$^^\t\2")
        buf.write("))^^ddhhppttvv\3\2))\3\2\62;\3\2\60\60\4\2GGgg\4\2--/")
        buf.write("/\3\2\f\f\4\2\f\f\16\17\5\2\n\13\16\17\"\"\3\3\f\f\3\2")
        buf.write("\16\17\2\u018c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\3s\3\2\2\2\5x\3\2\2\2\7~\3\2\2\2\t\u0085\3\2")
        buf.write("\2\2\13\u008a\3\2\2\2\r\u0091\3\2\2\2\17\u0098\3\2\2\2")
        buf.write("\21\u009c\3\2\2\2\23\u00a4\3\2\2\2\25\u00a9\3\2\2\2\27")
        buf.write("\u00ad\3\2\2\2\31\u00b3\3\2\2\2\33\u00b6\3\2\2\2\35\u00bc")
        buf.write("\3\2\2\2\37\u00c5\3\2\2\2!\u00c8\3\2\2\2#\u00cd\3\2\2")
        buf.write("\2%\u00d2\3\2\2\2\'\u00d8\3\2\2\2)\u00dc\3\2\2\2+\u00e0")
        buf.write("\3\2\2\2-\u00e4\3\2\2\2/\u00e7\3\2\2\2\61\u00e9\3\2\2")
        buf.write("\2\63\u00eb\3\2\2\2\65\u00ed\3\2\2\2\67\u00ef\3\2\2\2")
        buf.write("9\u00f1\3\2\2\2;\u00f3\3\2\2\2=\u00f6\3\2\2\2?\u00f9\3")
        buf.write("\2\2\2A\u00fc\3\2\2\2C\u00fe\3\2\2\2E\u0101\3\2\2\2G\u0103")
        buf.write("\3\2\2\2I\u0106\3\2\2\2K\u010a\3\2\2\2M\u010c\3\2\2\2")
        buf.write("O\u010e\3\2\2\2Q\u0110\3\2\2\2S\u0112\3\2\2\2U\u0114\3")
        buf.write("\2\2\2W\u011b\3\2\2\2Y\u0129\3\2\2\2[\u0131\3\2\2\2]\u0135")
        buf.write("\3\2\2\2_\u013c\3\2\2\2a\u0145\3\2\2\2c\u0147\3\2\2\2")
        buf.write("e\u0153\3\2\2\2g\u0159\3\2\2\2i\u015c\3\2\2\2k\u0166\3")
        buf.write("\2\2\2m\u0175\3\2\2\2o\u017a\3\2\2\2q\u017f\3\2\2\2st")
        buf.write("\7v\2\2tu\7t\2\2uv\7w\2\2vw\7g\2\2w\4\3\2\2\2xy\7h\2\2")
        buf.write("yz\7c\2\2z{\7n\2\2{|\7u\2\2|}\7g\2\2}\6\3\2\2\2~\177\7")
        buf.write("p\2\2\177\u0080\7w\2\2\u0080\u0081\7o\2\2\u0081\u0082")
        buf.write("\7d\2\2\u0082\u0083\7g\2\2\u0083\u0084\7t\2\2\u0084\b")
        buf.write("\3\2\2\2\u0085\u0086\7d\2\2\u0086\u0087\7q\2\2\u0087\u0088")
        buf.write("\7q\2\2\u0088\u0089\7n\2\2\u0089\n\3\2\2\2\u008a\u008b")
        buf.write("\7u\2\2\u008b\u008c\7v\2\2\u008c\u008d\7t\2\2\u008d\u008e")
        buf.write("\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090\7i\2\2\u0090\f")
        buf.write("\3\2\2\2\u0091\u0092\7t\2\2\u0092\u0093\7g\2\2\u0093\u0094")
        buf.write("\7v\2\2\u0094\u0095\7w\2\2\u0095\u0096\7t\2\2\u0096\u0097")
        buf.write("\7p\2\2\u0097\16\3\2\2\2\u0098\u0099\7x\2\2\u0099\u009a")
        buf.write("\7c\2\2\u009a\u009b\7t\2\2\u009b\20\3\2\2\2\u009c\u009d")
        buf.write("\7f\2\2\u009d\u009e\7{\2\2\u009e\u009f\7p\2\2\u009f\u00a0")
        buf.write("\7c\2\2\u00a0\u00a1\7o\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3")
        buf.write("\7e\2\2\u00a3\22\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7e\2\2\u00a8\24")
        buf.write("\3\2\2\2\u00a9\u00aa\7h\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\26\3\2\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7n\2\2\u00b2\30\3\2\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5")
        buf.write("\7{\2\2\u00b5\32\3\2\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8")
        buf.write("\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb")
        buf.write("\7m\2\2\u00bb\34\3\2\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be")
        buf.write("\7q\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4")
        buf.write("\7g\2\2\u00c4\36\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7h\2\2\u00c7 \3\2\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\"")
        buf.write("\3\2\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0")
        buf.write("\7k\2\2\u00d0\u00d1\7h\2\2\u00d1$\3\2\2\2\u00d2\u00d3")
        buf.write("\7d\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5\7i\2\2\u00d5\u00d6")
        buf.write("\7k\2\2\u00d6\u00d7\7p\2\2\u00d7&\3\2\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7f\2\2\u00db(\3")
        buf.write("\2\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7v\2\2\u00df*\3\2\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7f\2\2\u00e3,\3\2\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7t\2\2\u00e6.\3\2\2\2\u00e7\u00e8")
        buf.write("\7-\2\2\u00e8\60\3\2\2\2\u00e9\u00ea\7/\2\2\u00ea\62\3")
        buf.write("\2\2\2\u00eb\u00ec\7,\2\2\u00ec\64\3\2\2\2\u00ed\u00ee")
        buf.write("\7\61\2\2\u00ee\66\3\2\2\2\u00ef\u00f0\7\'\2\2\u00f08")
        buf.write("\3\2\2\2\u00f1\u00f2\7?\2\2\u00f2:\3\2\2\2\u00f3\u00f4")
        buf.write("\7?\2\2\u00f4\u00f5\7?\2\2\u00f5<\3\2\2\2\u00f6\u00f7")
        buf.write("\7>\2\2\u00f7\u00f8\7/\2\2\u00f8>\3\2\2\2\u00f9\u00fa")
        buf.write("\7#\2\2\u00fa\u00fb\7?\2\2\u00fb@\3\2\2\2\u00fc\u00fd")
        buf.write("\7>\2\2\u00fdB\3\2\2\2\u00fe\u00ff\7>\2\2\u00ff\u0100")
        buf.write("\7?\2\2\u0100D\3\2\2\2\u0101\u0102\7@\2\2\u0102F\3\2\2")
        buf.write("\2\u0103\u0104\7@\2\2\u0104\u0105\7?\2\2\u0105H\3\2\2")
        buf.write("\2\u0106\u0107\7\60\2\2\u0107\u0108\7\60\2\2\u0108\u0109")
        buf.write("\7\60\2\2\u0109J\3\2\2\2\u010a\u010b\7]\2\2\u010bL\3\2")
        buf.write("\2\2\u010c\u010d\7_\2\2\u010dN\3\2\2\2\u010e\u010f\7*")
        buf.write("\2\2\u010fP\3\2\2\2\u0110\u0111\7+\2\2\u0111R\3\2\2\2")
        buf.write("\u0112\u0113\7.\2\2\u0113T\3\2\2\2\u0114\u0118\t\2\2\2")
        buf.write("\u0115\u0117\t\3\2\2\u0116\u0115\3\2\2\2\u0117\u011a\3")
        buf.write("\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119V")
        buf.write("\3\2\2\2\u011a\u0118\3\2\2\2\u011b\u0123\t\4\2\2\u011c")
        buf.write("\u0122\n\5\2\2\u011d\u011e\7^\2\2\u011e\u0122\t\6\2\2")
        buf.write("\u011f\u0120\t\7\2\2\u0120\u0122\t\4\2\2\u0121\u011c\3")
        buf.write("\2\2\2\u0121\u011d\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0125")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0126\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127\t\4\2\2")
        buf.write("\u0127\u0128\b,\2\2\u0128X\3\2\2\2\u0129\u012b\5[.\2\u012a")
        buf.write("\u012c\5]/\2\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012e\3\2\2\2\u012d\u012f\5_\60\2\u012e\u012d\3\2\2\2")
        buf.write("\u012e\u012f\3\2\2\2\u012fZ\3\2\2\2\u0130\u0132\t\b\2")
        buf.write("\2\u0131\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0131")
        buf.write("\3\2\2\2\u0133\u0134\3\2\2\2\u0134\\\3\2\2\2\u0135\u0139")
        buf.write("\t\t\2\2\u0136\u0138\t\b\2\2\u0137\u0136\3\2\2\2\u0138")
        buf.write("\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a^\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013e\t\n\2")
        buf.write("\2\u013d\u013f\t\13\2\2\u013e\u013d\3\2\2\2\u013e\u013f")
        buf.write("\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u0142\t\b\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144`\3\2\2\2\u0145\u0146\t\f\2")
        buf.write("\2\u0146b\3\2\2\2\u0147\u0148\7%\2\2\u0148\u0149\7%\2")
        buf.write("\2\u0149\u014d\3\2\2\2\u014a\u014c\n\r\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u014d\3\2\2\2")
        buf.write("\u0150\u0151\b\62\3\2\u0151d\3\2\2\2\u0152\u0154\t\16")
        buf.write("\2\2\u0153\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157\3\2\2\2\u0157")
        buf.write("\u0158\b\63\3\2\u0158f\3\2\2\2\u0159\u015a\13\2\2\2\u015a")
        buf.write("\u015b\b\64\4\2\u015bh\3\2\2\2\u015c\u0160\t\4\2\2\u015d")
        buf.write("\u015f\5m\67\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2")
        buf.write("\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0163\3")
        buf.write("\2\2\2\u0162\u0160\3\2\2\2\u0163\u0164\5o8\2\u0164\u0165")
        buf.write("\b\65\5\2\u0165j\3\2\2\2\u0166\u016a\t\4\2\2\u0167\u0169")
        buf.write("\5m\67\2\u0168\u0167\3\2\2\2\u0169\u016c\3\2\2\2\u016a")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016d\3\2\2\2")
        buf.write("\u016c\u016a\3\2\2\2\u016d\u016e\5q9\2\u016e\u016f\b\66")
        buf.write("\6\2\u016fl\3\2\2\2\u0170\u0176\n\5\2\2\u0171\u0172\7")
        buf.write("^\2\2\u0172\u0176\t\6\2\2\u0173\u0174\t\7\2\2\u0174\u0176")
        buf.write("\t\4\2\2\u0175\u0170\3\2\2\2\u0175\u0171\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0176n\3\2\2\2\u0177\u017b\t\17\2\2\u0178")
        buf.write("\u0179\7\17\2\2\u0179\u017b\7\f\2\2\u017a\u0177\3\2\2")
        buf.write("\2\u017a\u0178\3\2\2\2\u017bp\3\2\2\2\u017c\u017d\7^\2")
        buf.write("\2\u017d\u0180\n\6\2\2\u017e\u0180\t\20\2\2\u017f\u017c")
        buf.write("\3\2\2\2\u017f\u017e\3\2\2\2\u0180r\3\2\2\2\23\2\u0118")
        buf.write("\u0121\u0123\u012b\u012e\u0133\u0139\u013e\u0143\u014d")
        buf.write("\u0155\u0160\u016a\u0175\u017a\u017f\7\3,\2\b\2\2\3\64")
        buf.write("\3\3\65\4\3\66\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQUAL = 28
    DEQUAL = 29
    ASSIGN = 30
    NEQUAL = 31
    LT = 32
    LTE = 33
    GT = 34
    GTE = 35
    SPREAD = 36
    LBRACKET = 37
    RBRACKET = 38
    LPAREN = 39
    RPAREN = 40
    COMMA = 41
    ID = 42
    STRING_LIT = 43
    NUMBER_LIT = 44
    NEWLINE = 45
    COMMENTS = 46
    WS = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'=='", "'<-'", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'...'", "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQUAL", "DEQUAL", "ASSIGN", "NEQUAL", 
            "LT", "LTE", "GT", "GTE", "SPREAD", "LBRACKET", "RBRACKET", 
            "LPAREN", "RPAREN", "COMMA", "ID", "STRING_LIT", "NUMBER_LIT", 
            "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                  "DEQUAL", "ASSIGN", "NEQUAL", "LT", "LTE", "GT", "GTE", 
                  "SPREAD", "LBRACKET", "RBRACKET", "LPAREN", "RPAREN", 
                  "COMMA", "ID", "STRING_LIT", "NUMBER_LIT", "INTPART", 
                  "DECPART", "EXPPART", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRING_ACCEPTED", 
                  "UNCLOSE_CHARACTER", "STRING_UNACCEPTED" ]

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
            actions[42] = self.STRING_LIT_action 
            actions[50] = self.ERROR_CHAR_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		print("==========================================");
            		print(self.text);
            		if(len(self.text)>=2 and self.text[-1]=='\n' and self.text [-2]=='\r'):
            			raise(UncloseString(self.text[1:-2]));
            		elif(self.text[-1]=='\n'):
            			raise(UncloseString(self.text[1:-1]));
            		else:
            			raise(UncloseString(self.text[1:]));	


     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	print("==========================================ILLEGAL==========================");
            	print(self.text[1:]);
            	raise IllegalEscape(self.text[1:])
            	print("==========================================ILLEGAL==========================");


     


