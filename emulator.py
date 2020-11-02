#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The module provides simulation of import function.
"""
import bin_format
import utils


# Assert function
def assert_recover_key(ctx, args):
    # [TODO]
    pass


def assert_sha256(ctx, args):
    # [TODO]
    pass


def assert_sha1(ctx, args):
    # [TODO]
    pass


def assert_sha512(ctx, args):
    # [TODO]
    pass


def assert_ripemd160(ctx, args):
    # [TODO]
    pass


def eosio_assert(ctx, args):
    expression = args[0]
    ctx.solver.add(expression == 1)


def eosio_assert_message(ctx, args):
    eosio_assert(ctx, args)


def eosio_assert_code(ctx, args):
    eosio_assert(ctx, args)


def eosio_exit(ctx, args):
    ctx.solver.add(0 == 1)  # add a false expression to pruning


def abort(ctx, args):
    eosio_assert(ctx, [0, 'abort()'])


# No effect function
def checktime(ctx, args):
    pass


def prints(ctx, args):
    pass


def prints_l(ctx, args):
    pass


def printi(ctx, args):
    pass


def printui(ctx, args):
    pass


def printi128(ctx, args):
    pass


def printui128(ctx, args):
    pass


def printsf(ctx, args):
    pass


def printdf(ctx, args):
    pass


def printqf(ctx, args):
    pass


def printn(ctx, args):
    pass


def printhex(ctx, args):
    pass


def set_resource_limits(ctx, args):
    pass


def set_blockchain_parameters_packed(ctx, args):
    pass


def set_privileged(ctx, args):
    pass


def preactivate_feature(ctx, args):
    pass


# Data reading functions
def get_generator():
    cur = 0
    while True:
        yield cur
        cur += 1


counter = get_generator()


def is_feature_active(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'is_feature_active_{next(counter)}')


def is_privileged(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'is_privileged_{next(counter)}')


def transaction_size(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'transaction_size_{next(counter)}')


def expiration(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'expiration_{next(counter)}')


def tapos_block_num(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'tapos_block_num_{next(counter)}')


def tapos_block_prefix(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'tapos_block_prefix_{next(counter)}')


def get_permission_last_used(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'get_permission_last_used_{next(counter)}')


def get_account_creation_time(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'get_account_creation_time_{next(counter)}')


def current_time(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'current_time_{next(counter)}')


def publication_time(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'publication_time_{next(counter)}')


def is_feature_activated(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'is_feature_activated_{next(counter)}')


def get_sender(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'get_sender_{next(counter)}')


def action_data_size(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'action_data_size_{next(counter)}')


def current_receiver(cttx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'current_receiver_{next(counter)}')


def has_auth(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'has_auth_{next(counter)}')


def is_account(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'is_account_{next(counter)}')


def cancel_deferred(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'cancel_deferred_{next(counter)}')


def memcmp(ctx, args):
    # [TODO] side effect
    return utils.gen_symbolic_value(bin_format.i32, f'memcmp_{next(counter)}')


def set_proposed_producers(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'set_proposed_producers_{next(counter)}')


def set_proposed_producers_ex(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'set_proposed_producers_ex_{next(counter)}')


def get_blockchain_parameters_packed(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'get_blockchain_parameters_packed_{next(counter)}')


def get_active_producers(ctx, args):
    return utils.gen_symbolic_value(bin_format.i64, f'get_active_producers_{next(counter)}')


# Computation functions
def ashlti3(ctx, args):
    # [TODO] Implement
    pass


def ashrti3(ctx, args):
    # [TODO] Implement
    pass


def lshlti3(ctx, args):
    # [TODO] Implement
    pass


def lshrti3(ctx, args):
    # [TODO] Implement
    pass


def divti3(ctx, args):
    # [TODO] Implement
    pass


def udivti3(ctx, args):
    # [TODO] Implement
    pass


def modti3(ctx, args):
    # [TODO] Implement
    pass


def umodti3(ctx, args):
    # [TODO] Implement
    pass


def multi3(ctx, args):
    # [TODO] Implement
    pass


def addtf3(ctx, args):
    # [TODO] Implement
    pass


def subtf3(ctx, args):
    # [TODO] Implement
    pass


def multf3(ctx, args):
    # [TODO] Implement
    pass


def divtf3(ctx, args):
    # [TODO] Implement
    pass


def eqtf2(ctx, args):
    # [TODO] Implement
    pass


def netf2(ctx, args):
    # [TODO] Implement
    pass


def getf2(ctx, args):
    # [TODO] Implement
    pass


def gttf2(ctx, args):
    # [TODO] Implement
    pass


def lttf2(ctx, args):
    # [TODO] Implement
    pass


def letf2(ctx, args):
    # [TODO] Implement
    pass


def cmptf2(ctx, args):
    # [TODO] Implement
    pass


def unordtf2(ctx, args):
    # [TODO] Implement
    pass


def negtf2(ctx, args):
    # [TODO] Implement
    pass


def floatsitf(ctx, args):
    # [TODO] Implement
    pass


def floatunsitf(ctx, args):
    # [TODO] Implement
    pass


def floatditf(ctx, args):
    # [TODO] Implement
    pass


def floatunditf(ctx, args):
    # [TODO] Implement
    pass


def floattidf(ctx, args):
    # [TODO] Implement
    pass


def floatuntidf(ctx, args):
    # [TODO] Implement
    pass


def floatsidf(ctx, args):
    # [TODO] Implement
    pass


def extendsftf2(ctx, args):
    # [TODO] Implement
    pass


def extenddftf2(ctx, args):
    # [TODO] Implement
    pass


def fixtfti(ctx, args):
    # [TODO] Implement
    pass


def fixtfdi(ctx, args):
    # [TODO] Implement
    pass


def fixtfsi(ctx, args):
    # [TODO] Implement
    pass


def fixunstfti(ctx, args):
    # [TODO] Implement
    pass


def fixunstfdi(ctx, args):
    # [TODO] Implement
    pass


def fixunstfsi(ctx, args):
    # [TODO] Implement
    pass


def fixsfti(ctx, args):
    # [TODO] Implement
    pass


def fixdfti(ctx, args):
    # [TODO] Implement
    pass


def fixunssfti(ctx, args):
    # [TODO] Implement
    pass


def fixunsdfti(ctx, args):
    # [TODO] Implement
    pass


def trunctfdf2(ctx, args):
    # if utils.is_all_real(args):
    #     return int(bin(args[0]) + bin(args[1])[2:], base=2)
    # args = [utils.to_symbolic(arg, 64) for arg in args]
    # z3.Concat(*args)
    pass


def trunctfsf2(ctx, args):
    # [TODO] Implement
    pass


def sha1(ctx, args):
    # [TODO] Implement
    pass


def sha256(ctx, args):
    # [TODO] Implement
    pass


def sha512(ctx, args):
    # [TODO] Implement
    pass


def ripemd160(ctx, args):
    # [TODO] Implement
    pass


# Data writing functions
def get_resource_limits(ctx, args):
    # [TODO]
    pass


def read_action_data(ctx, args):
    # [TODO]
    pass


def read_transaction(ctx, args):
    # [TODO]
    pass


def get_action(ctx, args):
    # [TODO] Implement
    pass


def get_context_free_data(ctx, args):
    # [TODO] Implement
    pass


def memcpy(ctx, args):
    # [TODO] Implement
    pass


def memmove(ctx, args):
    # [TODO]
    pass


def memset(ctx, args):
    # [TODO]
    pass


# Permission function
def check_transaction_authorization(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'check_transaction_authorization_{next(counter)}')


def check_permission_authorization(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'check_permission_authorization_{next(counter)}')


def require_auth(ctx, args):
    pass


def require_auth2(ctx, args):
    pass


# Other
def activate_feature(ctx, args):
    eosio_assert(ctx, [0])


def db_store_i64(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'db_store_i64_{next(counter)}')


def db_update_i64(ctx, args):
    pass


def db_remove_i64(ctx, args):
    pass


def db_get_i64(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'db_get_i64_{next(counter)}')


def db_next_i64(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'db_next_i64_{next(counter)}')


def db_previous_i64(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'db_previous_i64_{next(counter)}')


def db_find_i64(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'db_find_i64_{next(counter)}')


def db_lowerbound_i64(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'db_lowerbound_i64_{next(counter)}')


def db_upperbound_i64(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'db_upperbound_i64_{next(counter)}')


def db_end_i64(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'db_end_i64_{next(counter)}')


def recover_key(ctx, args):
    return utils.gen_symbolic_value(bin_format.i32, f'recover_key_{next(counter)}')


def require_recipient(ctx, args):
    pass


def send_inline(ctx, args):
    pass


def send_context_free_inline(ctx, args):
    pass


def send_deferred(ctx, args):
    pass
