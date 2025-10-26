import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):
    def test1(self):
        """Verifies empty input (no digits) → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator(""))

    def test2(self):
        """Verifies single non-digit present → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("a978146587240932"))

    def test3(self):
        """Verifies multiple non-digits present → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("a878b098c234f423"))

    def test4(self):
        """Verifies invalid issuer (prefix 3), len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("366330774851397"))

    def test5(self):
        """Verifies invalid issuer (prefix 3), len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("366938765432101"))

    def test6(self):
        """Verifies invalid issuer (prefix 3), len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3104332181960010"))

    def test7(self):
        """Verifies invalid issuer (prefix 3), len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3338908386379400"))

    def test8(self):
        """Verifies Visa (4) wrong len 15, Luhn pass → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("426542351161556"))

    def test9(self):
        """Verifies Visa (4) wrong len 15, Luhn fail → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("494078161849591"))

    def test10(self):
        """Verifies Visa (4) len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for Visa."""
        self.assertTrue(credit_card_validator("4310341316475255"))

    def test11(self):
        """Verifies Visa (4) len 16, Luhn fail → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("4471028082235966"))

    def test12(self):
        """Verifies Visa (4) wrong len 17, Luhn pass → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("45397712816052184"))

    def test13(self):
        """Verifies Visa (4) wrong len 17, Luhn fail → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("41250092614783903"))

    def test14(self):
        """Verifies '5' not 51–55, len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("523645087296401"))

    def test15(self):
        """Verifies '5' not 51–55, len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("557203918274615"))

    def test16(self):
        """Verifies MC (52xxxx) len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for MC."""
        self.assertTrue(credit_card_validator("5283104796152746"))

    def test17(self):
        """Verifies MC (53xxxx) len 16, Luhn fail → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("5319204861732057"))

    def test18(self):
        """Verifies invalid MC subrange 50, len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("501642837190451"))

    def test19(self):
        """Verifies invalid MC subrange 50, len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("509312476805233"))

    def test20(self):
        """Verifies invalid MC subrange 50, len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("5012387649123456"))

    def test21(self):
        """Verifies invalid MC subrange 50, len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("5049012376543210"))

    def test22(self):
        """Verifies MC 51 wrong len 15, Luhn pass → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("511203984761025"))

    def test23(self):
        """Verifies MC 51 wrong len 15, Luhn fail → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("519876234501117"))

    def test24(self):
        """Verifies MC 51 len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for MC."""
        self.assertTrue(credit_card_validator("5110456723894506"))

    def test25(self):
        """Verifies MC 51 len 16, Luhn fail → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("5123094786123458"))

    def test26(self):
        """Verifies MC 51 wrong len 17, Luhn pass → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("51120398476102543"))

    def test27(self):
        """Verifies MC 51 wrong len 17, Luhn fail → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("51098765432101239"))

    def test28(self):
        """Verifies invalid MC subrange 56, len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("561203984761045"))

    def test29(self):
        """Verifies invalid MC subrange 56, len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("569876234501131"))

    def test30(self):
        """Verifies invalid MC subrange 56, len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("5610456723894526"))

    def test31(self):
        """Verifies invalid MC subrange 56, len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("5623094786123498"))

    def test32(self):
        """Verifies MC 2220 (<2221) len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("22204321098765"))

    def test33(self):
        """Verifies MC 2220 (<2221) len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("222012345678901"))

    def test34(self):
        """Verifies MC 2220 (<2221) len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("2220123456789016"))

    def test35(self):
        """Verifies MC 2220 (<2221) len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("2220987654321094"))

    def test36(self):
        """Verifies MC 2221 (lower bound) len 15, Luhn pass → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("222115678901234"))

    def test37(self):
        """Verifies MC 2221 (lower bound) len 15, Luhn fail → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("222156789012347"))

    def test38(self):
        """Verifies MC 2221 len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for MC."""
        self.assertTrue(credit_card_validator("2221123498765436"))

    def test39(self):
        """Verifies MC 2221 len 16, Luhn fail → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("2221345678901234"))

    def test40(self):
        """Verifies MC 2221 len 17, Luhn pass → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("22211234567890123"))

    def test41(self):
        """Verifies MC 2221 len 17, Luhn fail → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("22219876543210987"))

    def test42(self):
        """Verifies MC 2721 (>2720) len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("272112345678901"))

    def test43(self):
        """Verifies MC 2721 (>2720) len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("272143210987653"))

    def test44(self):
        """Verifies MC 2721 (>2720) len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("2721123456789016"))

    def test45(self):
        """Verifies MC 2721 (>2720) len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("2721432109876548"))

    def test46(self):
        """Verifies invalid AmEx-like 33, len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("331234567890125"))

    def test47(self):
        """Verifies invalid AmEx-like 33, len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("339876543210117"))

    def test48(self):
        """Verifies invalid AmEx-like 33, len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3310456723894502"))

    def test49(self):
        """Verifies invalid AmEx-like 33, len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3323094786123490"))

    def test50(self):
        """Verifies AmEx (34) len 14, Luhn pass → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("34123456789012"))

    def test51(self):
        """Verifies AmEx (34) len 14, Luhn fail → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("34987654321019"))

    def test52(self):
        """Verifies AmEx (34) len 15, Luhn pass → True.
        Picked using credit card type partition. Correct value for AmEx."""
        self.assertTrue(credit_card_validator("341234567890125"))

    def test53(self):
        """Verifies AmEx (34) len 15, Luhn fail → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("347654321098137"))

    def test54(self):
        """Verifies AmEx (34) len 16, Luhn pass → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("3410456723894501"))

    def test55(self):
        """Verifies AmEx (34) len 16, Luhn fail → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("3423094786123493"))

    def test56(self):
        """Verifies invalid AmEx-like 36, len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("361234567890125"))

    def test57(self):
        """Verifies invalid AmEx-like 36, len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("369876543210133"))

    def test58(self):
        """Verifies invalid AmEx-like 36, len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3610456723894503"))

    def test59(self):
        """Verifies invalid AmEx-like 36, len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3623094786123495"))

    def test60(self):
        """Verifies AmEx (37) len 14, Luhn pass → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("37123456789012"))

    def test61(self):
        """Verifies AmEx (37) len 14, Luhn fail → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("37987654321018"))

    def test62(self):
        """Verifies AmEx (37) len 15, Luhn pass → True.
        Picked using credit card type partition. Correct value for AmEx."""
        self.assertTrue(credit_card_validator("371234567890125"))

    def test63(self):
        """Verifies AmEx (37) len 15, Luhn fail → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("377654321098137"))

    def test64(self):
        """Verifies AmEx (37) len 16, Luhn pass → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("3710456723894509"))

    def test65(self):
        """Verifies AmEx (37) len 16, Luhn fail → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("3723094786123491"))

    def test66(self):
        """Verifies invalid AmEx-like 38, len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("381234567890125"))

    def test67(self):
        """Verifies invalid AmEx-like 38, len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("389876543210131"))

    def test68(self):
        """Verifies invalid AmEx-like 38, len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3810456723894507"))

    def test69(self):
        """Verifies invalid AmEx-like 38, len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3823094786123499"))

    def test70(self):
        """Verifies MC upper bound 2720 len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for MC."""
        self.assertTrue(credit_card_validator("2720123456789015"))

    def test71(self):
        """Verifies Visa (4) wrong len 15 → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("412345678901234"))

    def test72(self):
        """Verifies all zeros rejected even if Luhn is 0 → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("0000000000000000"))

    def test73(self):
        """Verifies MC mid-range 2600 len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for MC."""
        self.assertTrue(credit_card_validator("2600123456789013"))

    def test74(self):
        """Verifies MC 55 (upper of 51–55) len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for MC."""
        self.assertTrue(credit_card_validator("5500000000000004"))

    def test75(self):
        """Verifies MC 2221 (lower bound) len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for MC."""
        self.assertTrue(credit_card_validator("2221123412341234"))

    def test76(self):
        """Verifies Visa overlength 20 digits → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("41111111111111111111"))

    def test77(self):
        """Verifies MC upper bound 2720 len 16, pass (duplicate) → True.
        Picked using credit card type partition."""
        self.assertTrue(credit_card_validator("2720123456789015"))

    def test78(self):
        """Verifies 371 (AmEx-like) with 16 digits → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3710000000000000"))

    def test79(self):
        """Verifies prefix '5' only (not 51–55), len 16 → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("5000000000000000"))

    def test80(self):
        """Verifies too short (9 digits) → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("412345678"))

    def test81(self):
        """Verifies Visa 19-digit (outside spec) → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("4000000000000000008"))

    def test82(self):
        """Verifies MC mid-range 2500 len 16, Luhn pass → True.
        Picked using credit card type partition. Correct value for MC."""
        self.assertTrue(credit_card_validator("2500123456789016"))

    def test83(self):
        """Verifies AmEx 37 known-valid len 15, Luhn pass → True.
        Picked using credit card type partition. Correct value for AmEx."""
        self.assertTrue(credit_card_validator("371449635398431"))

    def test84(self):
        """Verifies invalid issuer (prefix 3), len 17, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("30000000000000007"))

    def test85(self):
        """Verifies invalid issuer (prefix 3), len 17, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("30000000000000000"))

    # --- '5' not in 51–55 (e.g., 59…), lengths 16/17 ---
    def test86(self):
        """Verifies '5' not 51–55 len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("5900000000000000"))

    def test87(self):
        """Verifies '5' not 51–55 len 17, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("59000000000000006"))

    def test88(self):
        """Verifies '5' not 51–55 len 17, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("59000000000000000"))

    # --- MC invalid subranges 50 and 56 at 17 digits ---
    def test89(self):
        """Verifies MC subrange 50 len 17, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("50000000000000005"))

    def test90(self):
        """Verifies MC subrange 50 len 17, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("50000000000000000"))

    def test91(self):
        """Verifies MC subrange 56 len 17, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("56000000000000002"))

    def test92(self):
        """Verifies MC subrange 56 len 17, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("56000000000000000"))

    def test93(self):
        """Verifies MC 2220 (<2221) len 17, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("22200000000000002"))

    def test94(self):
        """Verifies MC 2220 (<2221) len 17, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("22200000000000000"))

    def test95(self):
        """Verifies MC 2721 (>2720) len 17, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("27210000000000009"))

    def test96(self):
        """Verifies MC 2721 (>2720) len 17, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("27210000000000000"))

    # --- MasterCard 55 (valid subrange) missing cases ---
    def test97(self):
        """Verifies MC 55 len 15, Luhn pass → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("550000000000004"))

    def test98(self):
        """Verifies MC 55 len 15, Luhn fail → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("550000000000000"))

    def test99(self):
        """Verifies MC 55 len 16, Luhn fail → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("5500000000000000"))

    def test100(self):
        """Verifies MC 55 len 17, Luhn pass → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("55000000000000004"))

    def test101(self):
        """Verifies MC 55 len 17, Luhn fail → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("55000000000000000"))

    # --- MasterCard 2720 (upper bound) missing cases ---
    def test102(self):
        """Verifies MC 2720 len 15, Luhn pass → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("272000000000000"))

    def test103(self):
        """Verifies MC 2720 len 15, Luhn fail → False.
        Picked using length partition (too short)."""
        self.assertFalse(credit_card_validator("272000000000000"))

    def test104(self):
        """Verifies MC 2720 len 16, Luhn fail → False.
        Picked using category partitioning."""
        self.assertFalse(credit_card_validator("2720000000000000"))

    def test105(self):
        """Verifies MC 2720 len 17, Luhn pass → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("27200000000000001"))

    def test106(self):
        """Verifies MC 2720 len 17, Luhn fail → False.
        Picked using length partition (too long)."""
        self.assertFalse(credit_card_validator("27200000000000000"))

    # --- AmEx-like invalid prefixes (33, 36, 38) at 14 digits ---
    def test107(self):
        """Verifies invalid 33 len 14, Luhn pass → False.
        Picked using credit card type partition and length partition."""
        self.assertFalse(credit_card_validator("33000000000001"))

    def test108(self):
        """Verifies invalid 33 len 14, Luhn fail → False.
        Picked using credit card type partition and length partition."""
        self.assertFalse(credit_card_validator("33000000000000"))

    def test109(self):
        """Verifies invalid 36 len 14, Luhn pass → False.
        Picked using credit card type partition and length partition."""
        self.assertFalse(credit_card_validator("36000000000008"))

    def test110(self):
        """Verifies invalid 36 len 14, Luhn fail → False.
        Picked using credit card type partition and length partition."""
        self.assertFalse(credit_card_validator("36000000000000"))

    def test111(self):
        """Verifies invalid 38 len 14, Luhn pass → False.
        Picked using credit card type partition and length partition."""
        self.assertFalse(credit_card_validator("38000000000006"))

    def test112(self):
        """Verifies invalid 38 len 14, Luhn fail → False.
        Picked using credit card type partition and length partition."""
        self.assertFalse(credit_card_validator("38000000000000"))

    # --- Prefix 35 (invalid for AmEx in this spec) at 14/15/16 digits ---
    def test113(self):
        """Verifies invalid 35 len 14, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("35000000000009"))

    def test114(self):
        """Verifies invalid 35 len 14, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("35000000000000"))

    def test115(self):
        """Verifies invalid 35 len 15, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("350000000000006"))

    def test116(self):
        """Verifies invalid 35 len 15, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("350000000000000"))

    def test117(self):
        """Verifies invalid 35 len 16, Luhn pass → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3500000000000009"))

    def test118(self):
        """Verifies invalid 35 len 16, Luhn fail → False.
        Picked using credit card type partition."""
        self.assertFalse(credit_card_validator("3500000000000000"))


if __name__ == "__main__":
    unittest.main()
