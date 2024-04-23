# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0196\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3f\n\3\3\4")
        buf.write("\3\4\3\4\3\4\5\4l\n\4\3\5\3\5\3\5\5\5q\n\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6y\n\6\3\6\3\6\5\6}\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\5\b\u0088\n\b\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u008e\n\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0096\n\n\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u009c\n\13\3\13\3\13\5\13\u00a0\n")
        buf.write("\13\3\13\3\13\5\13\u00a4\n\13\3\f\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u00ab\n\f\3\r\3\r\3\r\3\r\5\r\u00b1\n\r\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00b7\n\16\3\17\3\17\5\17\u00bb\n\17\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u00c1\n\20\3\21\3\21\5\21\u00c5\n\21")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00cd\n\23\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u00d7\n\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u00e2\n")
        buf.write("\25\3\25\3\25\3\25\3\25\5\25\u00e8\n\25\3\25\5\25\u00eb")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00f2\n\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u00f8\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0101\n\27\3\27\3\27\5\27\u0105\n\27\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\5\32\u010f\n\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\5\34\u011e\n\34\3\35\3\35\3\35\3\35\3\35\5")
        buf.write("\35\u0125\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u012c\n\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0134\n\37\f\37\16")
        buf.write("\37\u0137\13\37\3 \3 \3 \3 \3 \3 \7 \u013f\n \f \16 \u0142")
        buf.write("\13 \3!\3!\3!\3!\3!\3!\7!\u014a\n!\f!\16!\u014d\13!\3")
        buf.write("\"\3\"\3\"\5\"\u0152\n\"\3#\3#\3#\5#\u0157\n#\3$\3$\3")
        buf.write("$\3$\5$\u015d\n$\3$\5$\u0160\n$\3$\3$\3$\3$\3$\5$\u0167")
        buf.write("\n$\3%\3%\3%\3%\5%\u016d\n%\3&\3&\3&\3&\3\'\3\'\3\'\5")
        buf.write("\'\u0176\n\'\3\'\3\'\3(\3(\3(\3(\3(\5(\u017f\n(\3)\3)")
        buf.write("\3)\3)\5)\u0185\n)\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\7,\u0191")
        buf.write("\n,\f,\16,\u0194\13,\3,\2\5<>@-\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2")
        buf.write("\7\5\2##%)++\3\2\34\35\3\2\36\37\3\2 \"\3\2\n\f\2\u01a0")
        buf.write("\2[\3\2\2\2\4e\3\2\2\2\6k\3\2\2\2\bp\3\2\2\2\nr\3\2\2")
        buf.write("\2\f~\3\2\2\2\16\u0083\3\2\2\2\20\u008d\3\2\2\2\22\u008f")
        buf.write("\3\2\2\2\24\u0097\3\2\2\2\26\u00aa\3\2\2\2\30\u00b0\3")
        buf.write("\2\2\2\32\u00b6\3\2\2\2\34\u00ba\3\2\2\2\36\u00c0\3\2")
        buf.write("\2\2 \u00c4\3\2\2\2\"\u00c6\3\2\2\2$\u00c9\3\2\2\2&\u00d1")
        buf.write("\3\2\2\2(\u00dc\3\2\2\2*\u00f7\3\2\2\2,\u00f9\3\2\2\2")
        buf.write(".\u0106\3\2\2\2\60\u0109\3\2\2\2\62\u010c\3\2\2\2\64\u0112")
        buf.write("\3\2\2\2\66\u011d\3\2\2\28\u0124\3\2\2\2:\u012b\3\2\2")
        buf.write("\2<\u012d\3\2\2\2>\u0138\3\2\2\2@\u0143\3\2\2\2B\u0151")
        buf.write("\3\2\2\2D\u0156\3\2\2\2F\u0166\3\2\2\2H\u016c\3\2\2\2")
        buf.write("J\u016e\3\2\2\2L\u0172\3\2\2\2N\u017e\3\2\2\2P\u0184\3")
        buf.write("\2\2\2R\u0186\3\2\2\2T\u0188\3\2\2\2V\u018c\3\2\2\2XZ")
        buf.write("\7\6\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3")
        buf.write("\2\2\2][\3\2\2\2^_\5\4\3\2_`\7\2\2\3`\3\3\2\2\2ab\5\6")
        buf.write("\4\2bc\5\4\3\2cf\3\2\2\2df\5\6\4\2ea\3\2\2\2ed\3\2\2\2")
        buf.write("f\5\3\2\2\2gh\5\b\5\2hi\5V,\2il\3\2\2\2jl\5\24\13\2kg")
        buf.write("\3\2\2\2kj\3\2\2\2l\7\3\2\2\2mq\5\n\6\2nq\5\f\7\2oq\5")
        buf.write("\16\b\2pm\3\2\2\2pn\3\2\2\2po\3\2\2\2q\t\3\2\2\2rs\5R")
        buf.write("*\2sx\7\61\2\2tu\7.\2\2uv\5\20\t\2vw\7/\2\2wy\3\2\2\2")
        buf.write("xt\3\2\2\2xy\3\2\2\2y|\3\2\2\2z{\7$\2\2{}\58\35\2|z\3")
        buf.write("\2\2\2|}\3\2\2\2}\13\3\2\2\2~\177\7\16\2\2\177\u0080\7")
        buf.write("\61\2\2\u0080\u0081\7$\2\2\u0081\u0082\58\35\2\u0082\r")
        buf.write("\3\2\2\2\u0083\u0084\7\17\2\2\u0084\u0087\7\61\2\2\u0085")
        buf.write("\u0086\7$\2\2\u0086\u0088\58\35\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\17\3\2\2\2\u0089\u008a\7\3")
        buf.write("\2\2\u008a\u008b\7\60\2\2\u008b\u008e\5\20\t\2\u008c\u008e")
        buf.write("\7\3\2\2\u008d\u0089\3\2\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\21\3\2\2\2\u008f\u0090\5R*\2\u0090\u0095\7\61\2\2\u0091")
        buf.write("\u0092\7.\2\2\u0092\u0093\5\20\t\2\u0093\u0094\7/\2\2")
        buf.write("\u0094\u0096\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\23\3\2\2\2\u0097\u0098\7\20\2\2\u0098\u0099")
        buf.write("\7\61\2\2\u0099\u009b\7,\2\2\u009a\u009c\5\26\f\2\u009b")
        buf.write("\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d\u00a3\7-\2\2\u009e\u00a0\5V,\2\u009f\u009e\3\2")
        buf.write("\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a4")
        buf.write("\5 \21\2\u00a2\u00a4\5V,\2\u00a3\u009f\3\2\2\2\u00a3\u00a2")
        buf.write("\3\2\2\2\u00a4\25\3\2\2\2\u00a5\u00a6\5\22\n\2\u00a6\u00a7")
        buf.write("\7\60\2\2\u00a7\u00a8\5\26\f\2\u00a8\u00ab\3\2\2\2\u00a9")
        buf.write("\u00ab\5\22\n\2\u00aa\u00a5\3\2\2\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00ab\27\3\2\2\2\u00ac\u00ad\5\32\16\2\u00ad\u00ae")
        buf.write("\5\30\r\2\u00ae\u00b1\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0")
        buf.write("\u00ac\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\31\3\2\2\2\u00b2")
        buf.write("\u00b7\5\34\17\2\u00b3\u00b7\5&\24\2\u00b4\u00b7\5\36")
        buf.write("\20\2\u00b5\u00b7\5 \21\2\u00b6\u00b2\3\2\2\2\u00b6\u00b3")
        buf.write("\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7")
        buf.write("\33\3\2\2\2\u00b8\u00bb\5\"\22\2\u00b9\u00bb\5$\23\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\35\3\2\2\2\u00bc")
        buf.write("\u00c1\5(\25\2\u00bd\u00c1\5,\27\2\u00be\u00c1\5.\30\2")
        buf.write("\u00bf\u00c1\5\60\31\2\u00c0\u00bc\3\2\2\2\u00c0\u00bd")
        buf.write("\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write("\37\3\2\2\2\u00c2\u00c5\5\62\32\2\u00c3\u00c5\5\64\33")
        buf.write("\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5!\3\2")
        buf.write("\2\2\u00c6\u00c7\5\b\5\2\u00c7\u00c8\5V,\2\u00c8#\3\2")
        buf.write("\2\2\u00c9\u00ca\7\61\2\2\u00ca\u00cc\7,\2\2\u00cb\u00cd")
        buf.write("\5\66\34\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00ce\3\2\2\2\u00ce\u00cf\7-\2\2\u00cf\u00d0\5V,\2\u00d0")
        buf.write("%\3\2\2\2\u00d1\u00d6\7\61\2\2\u00d2\u00d3\7.\2\2\u00d3")
        buf.write("\u00d4\5\66\34\2\u00d4\u00d5\7/\2\2\u00d5\u00d7\3\2\2")
        buf.write("\2\u00d6\u00d2\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\u00d9\7$\2\2\u00d9\u00da\58\35\2\u00da")
        buf.write("\u00db\5V,\2\u00db\'\3\2\2\2\u00dc\u00dd\7\26\2\2\u00dd")
        buf.write("\u00de\7,\2\2\u00de\u00df\58\35\2\u00df\u00e1\7-\2\2\u00e0")
        buf.write("\u00e2\5V,\2\u00e1\u00e0\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e3\3\2\2\2\u00e3\u00e4\5\32\16\2\u00e4\u00e7\5*\26")
        buf.write("\2\u00e5\u00e6\7\27\2\2\u00e6\u00e8\5\32\16\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9")
        buf.write("\u00eb\5V,\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write(")\3\2\2\2\u00ec\u00ed\7\30\2\2\u00ed\u00ee\7,\2\2\u00ee")
        buf.write("\u00ef\58\35\2\u00ef\u00f1\7-\2\2\u00f0\u00f2\5V,\2\u00f1")
        buf.write("\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2")
        buf.write("\u00f3\u00f4\5\32\16\2\u00f4\u00f5\5*\26\2\u00f5\u00f8")
        buf.write("\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00ec\3\2\2\2\u00f7")
        buf.write("\u00f6\3\2\2\2\u00f8+\3\2\2\2\u00f9\u00fa\7\21\2\2\u00fa")
        buf.write("\u00fb\7\61\2\2\u00fb\u00fc\7\22\2\2\u00fc\u00fd\58\35")
        buf.write("\2\u00fd\u00fe\7\23\2\2\u00fe\u0100\58\35\2\u00ff\u0101")
        buf.write("\5V,\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0104\5\32\16\2\u0103\u0105\5V,\2\u0104")
        buf.write("\u0103\3\2\2\2\u0104\u0105\3\2\2\2\u0105-\3\2\2\2\u0106")
        buf.write("\u0107\7\24\2\2\u0107\u0108\5V,\2\u0108/\3\2\2\2\u0109")
        buf.write("\u010a\7\25\2\2\u010a\u010b\5V,\2\u010b\61\3\2\2\2\u010c")
        buf.write("\u010e\7\r\2\2\u010d\u010f\58\35\2\u010e\u010d\3\2\2\2")
        buf.write("\u010e\u010f\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\5")
        buf.write("V,\2\u0111\63\3\2\2\2\u0112\u0113\7\31\2\2\u0113\u0114")
        buf.write("\5V,\2\u0114\u0115\5\30\r\2\u0115\u0116\7\32\2\2\u0116")
        buf.write("\u0117\5V,\2\u0117\65\3\2\2\2\u0118\u0119\58\35\2\u0119")
        buf.write("\u011a\7\60\2\2\u011a\u011b\5\66\34\2\u011b\u011e\3\2")
        buf.write("\2\2\u011c\u011e\58\35\2\u011d\u0118\3\2\2\2\u011d\u011c")
        buf.write("\3\2\2\2\u011e\67\3\2\2\2\u011f\u0120\5:\36\2\u0120\u0121")
        buf.write("\7*\2\2\u0121\u0122\5:\36\2\u0122\u0125\3\2\2\2\u0123")
        buf.write("\u0125\5:\36\2\u0124\u011f\3\2\2\2\u0124\u0123\3\2\2\2")
        buf.write("\u01259\3\2\2\2\u0126\u0127\5<\37\2\u0127\u0128\t\2\2")
        buf.write("\2\u0128\u0129\5<\37\2\u0129\u012c\3\2\2\2\u012a\u012c")
        buf.write("\5<\37\2\u012b\u0126\3\2\2\2\u012b\u012a\3\2\2\2\u012c")
        buf.write(";\3\2\2\2\u012d\u012e\b\37\1\2\u012e\u012f\5> \2\u012f")
        buf.write("\u0135\3\2\2\2\u0130\u0131\f\4\2\2\u0131\u0132\t\3\2\2")
        buf.write("\u0132\u0134\5> \2\u0133\u0130\3\2\2\2\u0134\u0137\3\2")
        buf.write("\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136=\3")
        buf.write("\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139\b \1\2\u0139\u013a")
        buf.write("\5@!\2\u013a\u0140\3\2\2\2\u013b\u013c\f\4\2\2\u013c\u013d")
        buf.write("\t\4\2\2\u013d\u013f\5@!\2\u013e\u013b\3\2\2\2\u013f\u0142")
        buf.write("\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("?\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0144\b!\1\2\u0144")
        buf.write("\u0145\5B\"\2\u0145\u014b\3\2\2\2\u0146\u0147\f\4\2\2")
        buf.write("\u0147\u0148\t\5\2\2\u0148\u014a\5B\"\2\u0149\u0146\3")
        buf.write("\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014cA\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f")
        buf.write("\7\33\2\2\u014f\u0152\5B\"\2\u0150\u0152\5D#\2\u0151\u014e")
        buf.write("\3\2\2\2\u0151\u0150\3\2\2\2\u0152C\3\2\2\2\u0153\u0154")
        buf.write("\t\4\2\2\u0154\u0157\5D#\2\u0155\u0157\5F$\2\u0156\u0153")
        buf.write("\3\2\2\2\u0156\u0155\3\2\2\2\u0157E\3\2\2\2\u0158\u0160")
        buf.write("\7\61\2\2\u0159\u015a\7\61\2\2\u015a\u015c\7,\2\2\u015b")
        buf.write("\u015d\5N(\2\u015c\u015b\3\2\2\2\u015c\u015d\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\u0160\7-\2\2\u015f\u0158\3\2\2\2")
        buf.write("\u015f\u0159\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\7")
        buf.write(".\2\2\u0162\u0163\5N(\2\u0163\u0164\7/\2\2\u0164\u0167")
        buf.write("\3\2\2\2\u0165\u0167\5H%\2\u0166\u015f\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167G\3\2\2\2\u0168\u016d\7\61\2\2\u0169\u016d")
        buf.write("\5P)\2\u016a\u016d\5J&\2\u016b\u016d\5L\'\2\u016c\u0168")
        buf.write("\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016c")
        buf.write("\u016b\3\2\2\2\u016dI\3\2\2\2\u016e\u016f\7,\2\2\u016f")
        buf.write("\u0170\58\35\2\u0170\u0171\7-\2\2\u0171K\3\2\2\2\u0172")
        buf.write("\u0173\7\61\2\2\u0173\u0175\7,\2\2\u0174\u0176\5\66\34")
        buf.write("\2\u0175\u0174\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0178\7-\2\2\u0178M\3\2\2\2\u0179\u017f")
        buf.write("\58\35\2\u017a\u017b\58\35\2\u017b\u017c\7\60\2\2\u017c")
        buf.write("\u017d\5N(\2\u017d\u017f\3\2\2\2\u017e\u0179\3\2\2\2\u017e")
        buf.write("\u017a\3\2\2\2\u017fO\3\2\2\2\u0180\u0185\7\3\2\2\u0181")
        buf.write("\u0185\7\4\2\2\u0182\u0185\7\5\2\2\u0183\u0185\5T+\2\u0184")
        buf.write("\u0180\3\2\2\2\u0184\u0181\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0183\3\2\2\2\u0185Q\3\2\2\2\u0186\u0187\t\6\2")
        buf.write("\2\u0187S\3\2\2\2\u0188\u0189\7.\2\2\u0189\u018a\5\66")
        buf.write("\34\2\u018a\u018b\7/\2\2\u018bU\3\2\2\2\u018c\u0192\7")
        buf.write("\6\2\2\u018d\u018e\7\7\2\2\u018e\u0191\7\6\2\2\u018f\u0191")
        buf.write("\7\6\2\2\u0190\u018d\3\2\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193W\3\2\2\2\u0194\u0192\3\2\2\2/[ekpx|\u0087\u008d")
        buf.write("\u0095\u009b\u009f\u00a3\u00aa\u00b0\u00b6\u00ba\u00c0")
        buf.write("\u00c4\u00cc\u00d6\u00e1\u00e7\u00ea\u00f1\u00f7\u0100")
        buf.write("\u0104\u010e\u011d\u0124\u012b\u0135\u0140\u014b\u0151")
        buf.write("\u0156\u015c\u015f\u0166\u016c\u0175\u017e\u0184\u0190")
        buf.write("\u0192")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\n'", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "NUM_LIT", "BOOL_LIT", "STR_LIT", "NEWLN", 
                      "CMT", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "RES", "ASG", "UEQL", "LT", "LTE", "GT", "GTE", 
                      "CONCAT", "EQL", "CLB", "CRB", "SLB", "SRB", "COMMA", 
                      "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_program_stm = 1
    RULE_declare_stm = 2
    RULE_variables = 3
    RULE_keyword_var = 4
    RULE_normal_var = 5
    RULE_dynamic_var = 6
    RULE_num_list = 7
    RULE_parameter = 8
    RULE_function = 9
    RULE_param_list = 10
    RULE_stm_list = 11
    RULE_statement = 12
    RULE_declare_part_stm = 13
    RULE_flow_control_stm = 14
    RULE_func_control_stm = 15
    RULE_var_stm = 16
    RULE_func_stm = 17
    RULE_asg_stm = 18
    RULE_if_stm = 19
    RULE_elif_stm = 20
    RULE_for_stm = 21
    RULE_break_stm = 22
    RULE_continue_stm = 23
    RULE_return_stm = 24
    RULE_block_stm = 25
    RULE_expr_list = 26
    RULE_expression = 27
    RULE_expression1 = 28
    RULE_expression2 = 29
    RULE_expression3 = 30
    RULE_expression4 = 31
    RULE_expression5 = 32
    RULE_expression6 = 33
    RULE_expression7 = 34
    RULE_expression8 = 35
    RULE_sub_expr = 36
    RULE_func_call = 37
    RULE_index_operators = 38
    RULE_typ = 39
    RULE_normal_typ_name = 40
    RULE_arr_lit = 41
    RULE_ignore = 42

    ruleNames =  [ "program", "program_stm", "declare_stm", "variables", 
                   "keyword_var", "normal_var", "dynamic_var", "num_list", 
                   "parameter", "function", "param_list", "stm_list", "statement", 
                   "declare_part_stm", "flow_control_stm", "func_control_stm", 
                   "var_stm", "func_stm", "asg_stm", "if_stm", "elif_stm", 
                   "for_stm", "break_stm", "continue_stm", "return_stm", 
                   "block_stm", "expr_list", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "expression8", "sub_expr", 
                   "func_call", "index_operators", "typ", "normal_typ_name", 
                   "arr_lit", "ignore" ]

    EOF = Token.EOF
    NUM_LIT=1
    BOOL_LIT=2
    STR_LIT=3
    NEWLN=4
    CMT=5
    TRUE=6
    FALSE=7
    NUMBER=8
    BOOL=9
    STRING=10
    RETURN=11
    VAR=12
    DYNAMIC=13
    FUNC=14
    FOR=15
    UNTIL=16
    BY=17
    BREAK=18
    CONTINUE=19
    IF=20
    ELSE=21
    ELIF=22
    BEGIN=23
    END=24
    NOT=25
    AND=26
    OR=27
    ADD=28
    SUB=29
    MUL=30
    DIV=31
    MOD=32
    RES=33
    ASG=34
    UEQL=35
    LT=36
    LTE=37
    GT=38
    GTE=39
    CONCAT=40
    EQL=41
    CLB=42
    CRB=43
    SLB=44
    SRB=45
    COMMA=46
    ID=47
    WS=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Program_stmContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLN(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLN)
            else:
                return self.getToken(ZCodeParser.NEWLN, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLN:
                self.state = 86
                self.match(ZCodeParser.NEWLN)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.program_stm()
            self.state = 93
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Declare_stmContext,0)


        def program_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Program_stmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_stm" ):
                return visitor.visitProgram_stm(self)
            else:
                return visitor.visitChildren(self)




    def program_stm(self):

        localctx = ZCodeParser.Program_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_stm)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.declare_stm()
                self.state = 96
                self.program_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.declare_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_stm" ):
                return visitor.visitDeclare_stm(self)
            else:
                return visitor.visitChildren(self)




    def declare_stm(self):

        localctx = ZCodeParser.Declare_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare_stm)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.variables()
                self.state = 102
                self.ignore()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword_var(self):
            return self.getTypedRuleContext(ZCodeParser.Keyword_varContext,0)


        def normal_var(self):
            return self.getTypedRuleContext(ZCodeParser.Normal_varContext,0)


        def dynamic_var(self):
            return self.getTypedRuleContext(ZCodeParser.Dynamic_varContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = ZCodeParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variables)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.keyword_var()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.normal_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.dynamic_var()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Keyword_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_typ_name(self):
            return self.getTypedRuleContext(ZCodeParser.Normal_typ_nameContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def SLB(self):
            return self.getToken(ZCodeParser.SLB, 0)

        def num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Num_listContext,0)


        def SRB(self):
            return self.getToken(ZCodeParser.SRB, 0)

        def ASG(self):
            return self.getToken(ZCodeParser.ASG, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_keyword_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_var" ):
                return visitor.visitKeyword_var(self)
            else:
                return visitor.visitChildren(self)




    def keyword_var(self):

        localctx = ZCodeParser.Keyword_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_keyword_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.normal_typ_name()
            self.state = 113
            self.match(ZCodeParser.ID)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.SLB:
                self.state = 114
                self.match(ZCodeParser.SLB)
                self.state = 115
                self.num_list()
                self.state = 116
                self.match(ZCodeParser.SRB)


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASG:
                self.state = 120
                self.match(ZCodeParser.ASG)
                self.state = 121
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASG(self):
            return self.getToken(ZCodeParser.ASG, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_normal_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_var" ):
                return visitor.visitNormal_var(self)
            else:
                return visitor.visitChildren(self)




    def normal_var(self):

        localctx = ZCodeParser.Normal_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normal_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ZCodeParser.VAR)
            self.state = 125
            self.match(ZCodeParser.ID)
            self.state = 126
            self.match(ZCodeParser.ASG)
            self.state = 127
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASG(self):
            return self.getToken(ZCodeParser.ASG, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_var" ):
                return visitor.visitDynamic_var(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_var(self):

        localctx = ZCodeParser.Dynamic_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dynamic_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ZCodeParser.DYNAMIC)
            self.state = 130
            self.match(ZCodeParser.ID)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASG:
                self.state = 131
                self.match(ZCodeParser.ASG)
                self.state = 132
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Num_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_num_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_list" ):
                return visitor.visitNum_list(self)
            else:
                return visitor.visitChildren(self)




    def num_list(self):

        localctx = ZCodeParser.Num_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_num_list)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(ZCodeParser.NUM_LIT)
                self.state = 136
                self.match(ZCodeParser.COMMA)
                self.state = 137
                self.num_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(ZCodeParser.NUM_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_typ_name(self):
            return self.getTypedRuleContext(ZCodeParser.Normal_typ_nameContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def SLB(self):
            return self.getToken(ZCodeParser.SLB, 0)

        def num_list(self):
            return self.getTypedRuleContext(ZCodeParser.Num_listContext,0)


        def SRB(self):
            return self.getToken(ZCodeParser.SRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.normal_typ_name()
            self.state = 142
            self.match(ZCodeParser.ID)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.SLB:
                self.state = 143
                self.match(ZCodeParser.SLB)
                self.state = 144
                self.num_list()
                self.state = 145
                self.match(ZCodeParser.SRB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def CLB(self):
            return self.getToken(ZCodeParser.CLB, 0)

        def CRB(self):
            return self.getToken(ZCodeParser.CRB, 0)

        def func_control_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Func_control_stmContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(ZCodeParser.FUNC)
            self.state = 150
            self.match(ZCodeParser.ID)
            self.state = 151
            self.match(ZCodeParser.CLB)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0):
                self.state = 152
                self.param_list()


            self.state = 155
            self.match(ZCodeParser.CRB)
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLN:
                    self.state = 156
                    self.ignore()


                self.state = 159
                self.func_control_stm()
                pass

            elif la_ == 2:
                self.state = 160
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_list)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.parameter()
                self.state = 164
                self.match(ZCodeParser.COMMA)
                self.state = 165
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stm_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def stm_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stm_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stm_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStm_list" ):
                return visitor.visitStm_list(self)
            else:
                return visitor.visitChildren(self)




    def stm_list(self):

        localctx = ZCodeParser.Stm_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stm_list)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.statement()
                self.state = 171
                self.stm_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_part_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Declare_part_stmContext,0)


        def asg_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Asg_stmContext,0)


        def flow_control_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Flow_control_stmContext,0)


        def func_control_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Func_control_stmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.declare_part_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.asg_stm()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.flow_control_stm()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.func_control_stm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_part_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Var_stmContext,0)


        def func_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Func_stmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declare_part_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_part_stm" ):
                return visitor.visitDeclare_part_stm(self)
            else:
                return visitor.visitChildren(self)




    def declare_part_stm(self):

        localctx = ZCodeParser.Declare_part_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_declare_part_stm)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.var_stm()
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.func_stm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Flow_control_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stm(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmContext,0)


        def for_stm(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmContext,0)


        def break_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmContext,0)


        def continue_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_flow_control_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlow_control_stm" ):
                return visitor.visitFlow_control_stm(self)
            else:
                return visitor.visitChildren(self)




    def flow_control_stm(self):

        localctx = ZCodeParser.Flow_control_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_flow_control_stm)
        try:
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.if_stm()
                pass
            elif token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.for_stm()
                pass
            elif token in [ZCodeParser.BREAK]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.break_stm()
                pass
            elif token in [ZCodeParser.CONTINUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.continue_stm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_control_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmContext,0)


        def block_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_control_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_control_stm" ):
                return visitor.visitFunc_control_stm(self)
            else:
                return visitor.visitChildren(self)




    def func_control_stm(self):

        localctx = ZCodeParser.Func_control_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_control_stm)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.return_stm()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.block_stm()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(ZCodeParser.VariablesContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_stm" ):
                return visitor.visitVar_stm(self)
            else:
                return visitor.visitChildren(self)




    def var_stm(self):

        localctx = ZCodeParser.Var_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.variables()
            self.state = 197
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def CLB(self):
            return self.getToken(ZCodeParser.CLB, 0)

        def CRB(self):
            return self.getToken(ZCodeParser.CRB, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_stm" ):
                return visitor.visitFunc_stm(self)
            else:
                return visitor.visitChildren(self)




    def func_stm(self):

        localctx = ZCodeParser.Func_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(ZCodeParser.ID)
            self.state = 200
            self.match(ZCodeParser.CLB)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.BOOL_LIT) | (1 << ZCodeParser.STR_LIT) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.CLB) | (1 << ZCodeParser.SLB) | (1 << ZCodeParser.ID))) != 0):
                self.state = 201
                self.expr_list()


            self.state = 204
            self.match(ZCodeParser.CRB)
            self.state = 205
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asg_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASG(self):
            return self.getToken(ZCodeParser.ASG, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def SLB(self):
            return self.getToken(ZCodeParser.SLB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def SRB(self):
            return self.getToken(ZCodeParser.SRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_asg_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsg_stm" ):
                return visitor.visitAsg_stm(self)
            else:
                return visitor.visitChildren(self)




    def asg_stm(self):

        localctx = ZCodeParser.Asg_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_asg_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(ZCodeParser.ID)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.SLB:
                self.state = 208
                self.match(ZCodeParser.SLB)
                self.state = 209
                self.expr_list()
                self.state = 210
                self.match(ZCodeParser.SRB)


            self.state = 214
            self.match(ZCodeParser.ASG)
            self.state = 215
            self.expression()
            self.state = 216
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def CLB(self):
            return self.getToken(ZCodeParser.CLB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CRB(self):
            return self.getToken(ZCodeParser.CRB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def elif_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stm" ):
                return visitor.visitIf_stm(self)
            else:
                return visitor.visitChildren(self)




    def if_stm(self):

        localctx = ZCodeParser.If_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ZCodeParser.IF)
            self.state = 219
            self.match(ZCodeParser.CLB)
            self.state = 220
            self.expression()
            self.state = 221
            self.match(ZCodeParser.CRB)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLN:
                self.state = 222
                self.ignore()


            self.state = 225
            self.statement()
            self.state = 226
            self.elif_stm()
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 227
                self.match(ZCodeParser.ELSE)
                self.state = 228
                self.statement()


            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 231
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def CLB(self):
            return self.getToken(ZCodeParser.CLB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CRB(self):
            return self.getToken(ZCodeParser.CRB, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elif_stm(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stm" ):
                return visitor.visitElif_stm(self)
            else:
                return visitor.visitChildren(self)




    def elif_stm(self):

        localctx = ZCodeParser.Elif_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_elif_stm)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(ZCodeParser.ELIF)
                self.state = 235
                self.match(ZCodeParser.CLB)
                self.state = 236
                self.expression()
                self.state = 237
                self.match(ZCodeParser.CRB)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLN:
                    self.state = 238
                    self.ignore()


                self.state = 241
                self.statement()
                self.state = 242
                self.elif_stm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stm" ):
                return visitor.visitFor_stm(self)
            else:
                return visitor.visitChildren(self)




    def for_stm(self):

        localctx = ZCodeParser.For_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ZCodeParser.FOR)
            self.state = 248
            self.match(ZCodeParser.ID)
            self.state = 249
            self.match(ZCodeParser.UNTIL)
            self.state = 250
            self.expression()
            self.state = 251
            self.match(ZCodeParser.BY)
            self.state = 252
            self.expression()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLN:
                self.state = 253
                self.ignore()


            self.state = 256
            self.statement()
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 257
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stm" ):
                return visitor.visitBreak_stm(self)
            else:
                return visitor.visitChildren(self)




    def break_stm(self):

        localctx = ZCodeParser.Break_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_break_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(ZCodeParser.BREAK)
            self.state = 261
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stm" ):
                return visitor.visitContinue_stm(self)
            else:
                return visitor.visitChildren(self)




    def continue_stm(self):

        localctx = ZCodeParser.Continue_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continue_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(ZCodeParser.CONTINUE)
            self.state = 264
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stm" ):
                return visitor.visitReturn_stm(self)
            else:
                return visitor.visitChildren(self)




    def return_stm(self):

        localctx = ZCodeParser.Return_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_return_stm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(ZCodeParser.RETURN)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.BOOL_LIT) | (1 << ZCodeParser.STR_LIT) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.CLB) | (1 << ZCodeParser.SLB) | (1 << ZCodeParser.ID))) != 0):
                self.state = 267
                self.expression()


            self.state = 270
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def stm_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stm_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stm" ):
                return visitor.visitBlock_stm(self)
            else:
                return visitor.visitChildren(self)




    def block_stm(self):

        localctx = ZCodeParser.Block_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.BEGIN)
            self.state = 273
            self.ignore()
            self.state = 274
            self.stm_list()
            self.state = 275
            self.match(ZCodeParser.END)
            self.state = 276
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr_list)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.expression()
                self.state = 279
                self.match(ZCodeParser.COMMA)
                self.state = 280
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.expression1()
                self.state = 286
                self.match(ZCodeParser.CONCAT)
                self.state = 287
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def RES(self):
            return self.getToken(ZCodeParser.RES, 0)

        def EQL(self):
            return self.getToken(ZCodeParser.EQL, 0)

        def UEQL(self):
            return self.getToken(ZCodeParser.UEQL, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.expression2(0)
                self.state = 293
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.RES) | (1 << ZCodeParser.UEQL) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.EQL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 294
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 302
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 303
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 304
                    self.expression3(0) 
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 318
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 313
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 314
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 315
                    self.expression4(0) 
                self.state = 320
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 324
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 325
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 326
                    self.expression5() 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression5)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(ZCodeParser.NOT)
                self.state = 333
                self.expression5()
                pass
            elif token in [ZCodeParser.NUM_LIT, ZCodeParser.BOOL_LIT, ZCodeParser.STR_LIT, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.CLB, ZCodeParser.SLB, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.expression6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 338
                self.expression6()
                pass
            elif token in [ZCodeParser.NUM_LIT, ZCodeParser.BOOL_LIT, ZCodeParser.STR_LIT, ZCodeParser.CLB, ZCodeParser.SLB, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLB(self):
            return self.getToken(ZCodeParser.SLB, 0)

        def index_operators(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Index_operatorsContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,i)


        def SRB(self):
            return self.getToken(ZCodeParser.SRB, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def CLB(self):
            return self.getToken(ZCodeParser.CLB, 0)

        def CRB(self):
            return self.getToken(ZCodeParser.CRB, 0)

        def expression8(self):
            return self.getTypedRuleContext(ZCodeParser.Expression8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 342
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 343
                    self.match(ZCodeParser.ID)
                    self.state = 344
                    self.match(ZCodeParser.CLB)
                    self.state = 346
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.BOOL_LIT) | (1 << ZCodeParser.STR_LIT) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.CLB) | (1 << ZCodeParser.SLB) | (1 << ZCodeParser.ID))) != 0):
                        self.state = 345
                        self.index_operators()


                    self.state = 348
                    self.match(ZCodeParser.CRB)
                    pass


                self.state = 351
                self.match(ZCodeParser.SLB)
                self.state = 352
                self.index_operators()
                self.state = 353
                self.match(ZCodeParser.SRB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.expression8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sub_exprContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = ZCodeParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression8)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.typ()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.sub_expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLB(self):
            return self.getToken(ZCodeParser.CLB, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CRB(self):
            return self.getToken(ZCodeParser.CRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sub_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub_expr" ):
                return visitor.visitSub_expr(self)
            else:
                return visitor.visitChildren(self)




    def sub_expr(self):

        localctx = ZCodeParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_sub_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(ZCodeParser.CLB)
            self.state = 365
            self.expression()
            self.state = 366
            self.match(ZCodeParser.CRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def CLB(self):
            return self.getToken(ZCodeParser.CLB, 0)

        def CRB(self):
            return self.getToken(ZCodeParser.CRB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZCodeParser.ID)
            self.state = 369
            self.match(ZCodeParser.CLB)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.BOOL_LIT) | (1 << ZCodeParser.STR_LIT) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.CLB) | (1 << ZCodeParser.SLB) | (1 << ZCodeParser.ID))) != 0):
                self.state = 370
                self.expr_list()


            self.state = 373
            self.match(ZCodeParser.CRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operators(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = ZCodeParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_index_operators)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.expression()
                self.state = 377
                self.match(ZCodeParser.COMMA)
                self.state = 378
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(ZCodeParser.BOOL_LIT, 0)

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_litContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_typ)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(ZCodeParser.BOOL_LIT)
                pass
            elif token in [ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.match(ZCodeParser.STR_LIT)
                pass
            elif token in [ZCodeParser.SLB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.arr_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_typ_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_normal_typ_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_typ_name" ):
                return visitor.visitNormal_typ_name(self)
            else:
                return visitor.visitChildren(self)




    def normal_typ_name(self):

        localctx = ZCodeParser.Normal_typ_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_normal_typ_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLB(self):
            return self.getToken(ZCodeParser.SLB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def SRB(self):
            return self.getToken(ZCodeParser.SRB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = ZCodeParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(ZCodeParser.SLB)
            self.state = 391
            self.expr_list()
            self.state = 392
            self.match(ZCodeParser.SRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLN(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLN)
            else:
                return self.getToken(ZCodeParser.NEWLN, i)

        def CMT(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.CMT)
            else:
                return self.getToken(ZCodeParser.CMT, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(ZCodeParser.NEWLN)
            self.state = 400
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 398
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZCodeParser.CMT]:
                        self.state = 395
                        self.match(ZCodeParser.CMT)
                        self.state = 396
                        self.match(ZCodeParser.NEWLN)
                        pass
                    elif token in [ZCodeParser.NEWLN]:
                        self.state = 397
                        self.match(ZCodeParser.NEWLN)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 402
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.expression2_sempred
        self._predicates[30] = self.expression3_sempred
        self._predicates[31] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




