from . import charbase


class TestOriginalChartests(charbase.PlyCharCase):
    def test_lex_closure(self):
        self._execute_file("lex_closure.py")

    def test_lex_doc1(self):
        self._execute_file("lex_doc1.py")

    def test_lex_dup1(self):
        self._execute_file("lex_dup1.py")

    def test_lex_dup2(self):
        self._execute_file("lex_dup2.py")

    def test_lex_dup3(self):
        self._execute_file("lex_dup3.py")

    def test_lex_empty(self):
        self._execute_file("lex_empty.py")

    def test_lex_error1(self):
        self._execute_file("lex_error1.py")

    def test_lex_error2(self):
        self._execute_file("lex_error2.py")

    def test_lex_error3(self):
        self._execute_file("lex_error3.py")

    def test_lex_error4(self):
        self._execute_file("lex_error4.py")

    def test_lex_hedit(self):
        self._execute_file("lex_hedit.py")

    def test_lex_ignore2(self):
        self._execute_file("lex_ignore2.py")

    def test_lex_ignore(self):
        self._execute_file("lex_ignore.py")

    def test_lex_literal1(self):
        self._execute_file("lex_literal1.py")

    def test_lex_literal2(self):
        self._execute_file("lex_literal2.py")

    def test_lex_literal3(self):
        self._execute_file("lex_literal3.py")

    def test_lex_many_tokens(self):
        self._execute_file("lex_many_tokens.py")

    def test_lex_module_import(self):
        self._execute_file("lex_module_import.py")

    def test_lex_module(self):
        self._execute_file("lex_module.py")

    def test_lex_object(self):
        self._execute_file("lex_object.py")

    def test_lex_opt_alias(self):
        self._execute_file("lex_opt_alias.py")

    def test_lex_optimize2(self):
        self._execute_file("lex_optimize2.py")

    def test_lex_optimize3(self):
        self._execute_file("lex_optimize3.py")

    def test_lex_optimize(self):
        self._execute_file("lex_optimize.py")

    def test_lex_re1(self):
        self._execute_file("lex_re1.py")

    def test_lex_re2(self):
        self._execute_file("lex_re2.py")

    def test_lex_re3(self):
        self._execute_file("lex_re3.py")

    def test_lex_rule1(self):
        self._execute_file("lex_rule1.py")

    def test_lex_rule2(self):
        self._execute_file("lex_rule2.py")

    def test_lex_rule3(self):
        self._execute_file("lex_rule3.py")

    def test_lex_state1(self):
        self._execute_file("lex_state1.py")

    def test_lex_state2(self):
        self._execute_file("lex_state2.py")

    def test_lex_state3(self):
        self._execute_file("lex_state3.py")

    def test_lex_state4(self):
        self._execute_file("lex_state4.py")

    def test_lex_state5(self):
        self._execute_file("lex_state5.py")

    def test_lex_state_noerror(self):
        self._execute_file("lex_state_noerror.py")

    def test_lex_state_norule(self):
        self._execute_file("lex_state_norule.py")

    def test_lex_state_try(self):
        self._execute_file("lex_state_try.py")

    def test_lex_token1(self):
        self._execute_file("lex_token1.py")

    def test_lex_token2(self):
        self._execute_file("lex_token2.py")

    def test_lex_token3(self):
        self._execute_file("lex_token3.py")

    def test_lex_token4(self):
        self._execute_file("lex_token4.py")

    def test_lex_token5(self):
        self._execute_file("lex_token5.py")

    def test_lex_token_dup(self):
        self._execute_file("lex_token_dup.py")

    def test_yacc_badargs(self):
        self._execute_file("yacc_badargs.py")

    def test_yacc_badid(self):
        self._execute_file("yacc_badid.py")

    def test_yacc_badprec2(self):
        self._execute_file("yacc_badprec2.py")

    def test_yacc_badprec3(self):
        self._execute_file("yacc_badprec3.py")

    def test_yacc_badprec(self):
        self._execute_file("yacc_badprec.py")

    def test_yacc_badrule(self):
        self._execute_file("yacc_badrule.py")

    def test_yacc_badtok(self):
        self._execute_file("yacc_badtok.py")

    def test_yacc_dup(self):
        self._execute_file("yacc_dup.py")

    def test_yacc_error1(self):
        self._execute_file("yacc_error1.py")

    def test_yacc_error2(self):
        self._execute_file("yacc_error2.py")

    def test_yacc_error3(self):
        self._execute_file("yacc_error3.py")

    def test_yacc_error4(self):
        self._execute_file("yacc_error4.py")

    def test_yacc_error5(self):
        self._execute_file("yacc_error5.py")

    def test_yacc_error6(self):
        self._execute_file("yacc_error6.py")

    def test_yacc_error7(self):
        self._execute_file("yacc_error7.py")

    def test_yacc_inf(self):
        self._execute_file("yacc_inf.py")

    def test_yacc_literal(self):
        self._execute_file("yacc_literal.py")

    def test_yacc_misplaced(self):
        self._execute_file("yacc_misplaced.py")

    def test_yacc_missing1(self):
        self._execute_file("yacc_missing1.py")

    def test_yacc_nested(self):
        self._execute_file("yacc_nested.py")

    def test_yacc_nodoc(self):
        self._execute_file("yacc_nodoc.py")

    def test_yacc_noerror(self):
        self._execute_file("yacc_noerror.py")

    def test_yacc_nop(self):
        self._execute_file("yacc_nop.py")

    def test_yacc_notfunc(self):
        self._execute_file("yacc_notfunc.py")

    def test_yacc_notok(self):
        self._execute_file("yacc_notok.py")

    def test_yacc_prec1(self):
        self._execute_file("yacc_prec1.py")

    def test_yacc_rr(self):
        self._execute_file("yacc_rr.py")

    def test_yacc_rr_unused(self):
        self._execute_file("yacc_rr_unused.py")

    def test_yacc_simple(self):
        self._execute_file("yacc_simple.py")

    def test_yacc_sr(self):
        self._execute_file("yacc_sr.py")

    def test_yacc_term1(self):
        self._execute_file("yacc_term1.py")

    def test_yacc_unicode_literals(self):
        self._execute_file("yacc_unicode_literals.py")

    def test_yacc_unused(self):
        self._execute_file("yacc_unused.py")

    def test_yacc_unused_rule(self):
        self._execute_file("yacc_unused_rule.py")

    def test_yacc_uprec2(self):
        self._execute_file("yacc_uprec2.py")

    def test_yacc_uprec(self):
        self._execute_file("yacc_uprec.py")

