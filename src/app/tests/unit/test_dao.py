import unittest
from datetime import datetime

import src.app.connect as connect


class TestConnect(unittest.TestCase):
    def test_base_connect(self):
        connection = connect.connect()
        self.assertFalse(None, connection)

    def test_musician_connect(self):
        connection = connect.connect_musician()
        self.assertFalse(None, connection)

    def test_owner_connect(self):
        connection = connect.connect_owner()
        self.assertFalse(None, connection)

    def test_admin_connect(self):
        connection = connect.connect_admin()
        self.assertFalse(None, connection)


class TestAccQueries(unittest.TestCase):
    def test_sign_in(self):
        # arrange
        mail = "nura.alexevna@yandex.ru"
        password = "1234"
        # act
        acc = connect.sign_in(mail, password)
        # assert
        self.assertEqual(acc.id, 1001)

    def test_wrong_sign_in(self):
        mail = "nura.alexevna@yandex.ru"
        password = "wrong password"
        acc = connect.sign_in(mail, password)
        self.assertEqual(acc.id, -1)

    def test_sign_up(self):
        acc = connect.Account()
        acc.fio = "aaaa"
        acc.phone = "1234567"
        acc.mail = "some.mail@gmail.com"
        acc.password = "testing"
        acc.type = "musician"
        err_code = connect.sign_up(acc)
        self.assertEqual(err_code, 0)

    def test_sign_up_exist(self):
        acc = connect.Account()
        acc.fio = "aaaa"
        acc.phone = "1234567"
        acc.mail = "nura.alexevna@yandex.ru"
        acc.password = "testing"
        acc.type = "musician"
        err_code = connect.sign_up(acc)
        self.assertEqual(err_code, 1)


class TestBaseQueries(unittest.TestCase):
    def test_reg_base(self):
        base = connect.RehBase()
        base.owner_id = 1
        base.name = "HighGain"
        base.address = "Volgogradka"
        base.phone = "97654"
        base.mail = "test.mail@gmail.com"
        conn = connect.connect()

        err_code = connect.reg_base(conn, base)
        conn.close()

        self.assertEqual(err_code, 0)

    def test_reg_base_exist(self):
        base = connect.RehBase()
        base.owner_id = 1
        base.name = "HighGain"
        base.address = "Volgogradka"
        base.phone = "97654"
        base.mail = "test.mail@gmail.com"
        conn = connect.connect()

        err_code = connect.reg_base(conn, base)
        conn.close()

        self.assertEqual(err_code, 1)

    def test_get_bases(self):
        acc_id = 8
        conn = connect.connect()
        base_ids = [560, 763]

        res = connect.get_bases(conn, acc_id)
        res = [res[0][0], res[1][0]]
        conn.close()

        self.assertEqual(res, base_ids)

    def test_bases_by_name(self):
        base_name = "kmwhb"
        conn = connect.connect()
        base_ids = [1000]

        res = connect.bases_by_name(conn, base_name)
        res = [res[0][0]]
        conn.close()

        self.assertEqual(res, base_ids)

    def test_base_info(self):
        base_id = 1000
        conn = connect.connect()
        base = [("kmwhb", "ayqdpcxfpf", "+7-944-084-68-88", "ifk@mail.ru")]

        res = connect.base_info(conn, base_id)
        conn.close()

        self.assertEqual(res, base)

    def test_del_base(self):
        base_id = 1001
        conn = connect.connect()
        err_code = connect.del_base(conn, base_id)
        self.assertEqual(err_code, 0)


class TestRoomQueries(unittest.TestCase):
    def test_add_room(self):
        room = connect.Room()
        room.base_id = 1
        room.name = "Yellow"
        room.type = "band"
        room.area = 23
        room.cost = 1500
        conn = connect.connect()

        err_code = connect.add_room(conn, room)
        conn.close()

        self.assertEqual(err_code, 0)

    def test_add_room_exist(self):
        room = connect.Room()
        room.base_id = 1
        room.name = "Yellow"
        room.type = "band"
        room.area = 23
        room.cost = 1500
        conn = connect.connect()

        err_code = connect.add_room(conn, room)
        conn.close()

        self.assertEqual(err_code, 1)

    def test_get_all_rooms(self):
        conn = connect.connect()
        room_ids = [i+1 for i in range(1000)]

        res = connect.get_all_rooms(conn)
        res_ids = [res[i][0] for i in range(1000)]
        conn.close()

        self.assertEqual(res_ids, room_ids)

    def test_room_info(self):
        room_id = 1000
        conn = connect.connect()
        room = [("swoft", "drum", 16, 472, "sjtpy", "nueupkvrvc")]

        res = connect.room_info(conn, room_id)
        conn.close()

        self.assertEqual(res, room)

    def test_rooms_by_base(self):
        base_id = 6
        conn = connect.connect()
        room_ids = [329, 664]

        res = connect.rooms_by_base(conn, base_id)
        res = [res[0][0], res[1][0]]
        conn.close()

        self.assertEqual(res, room_ids)


class TestGearQueries(unittest.TestCase):
    def test_add_gear(self):
        room_name = "vunno"
        base_id = 727
        gear = connect.Gear()
        gear.type = "amp"
        gear.brand = "Orange"
        gear.amount = 1
        conn = connect.connect()

        err_code = connect.add_gear(conn, gear, room_name, base_id)
        conn.close()

        self.assertEqual(err_code, 0)

    def test_add_gear_exist(self):
        room_name = "vunno"
        base_id = 727
        gear = connect.Gear()
        gear.type = "amp"
        gear.brand = "Orange"
        gear.amount = 1
        conn = connect.connect()

        err_code = connect.add_gear(conn, gear, room_name, base_id)
        conn.close()

        self.assertEqual(err_code, 1)

    def test_add_gear_room_not_exist(self):
        room_name = "Black"
        base_id = 1
        gear = connect.Gear()
        gear.type = "amp"
        gear.brand = "Orange"
        gear.amount = 1
        conn = connect.connect()

        err_code = connect.add_gear(conn, gear, room_name, base_id)
        conn.close()

        self.assertEqual(err_code, 2)

    def test_gear_info(self):
        room_id = 4
        conn = connect.connect()
        gear = [("mic", "qxseg", 1)]

        res = connect.gear_info(conn, room_id)
        conn.close()

        self.assertEqual(res, gear)


class TestRehearsalQueries(unittest.TestCase):
    def test_book(self):
        reh = connect.Rehearsal()
        reh.musician_id = 4
        reh.room_id = 1
        reh.date = "2022-11-01 12:00:00"
        conn = connect.connect()

        err_code = connect.book(conn, reh)
        conn.close()

        self.assertEqual(err_code, 0)

    def test_book_exist(self):
        reh = connect.Rehearsal()
        reh.musician_id = 4
        reh.room_id = 1
        reh.date = "2022-11-01 12:00:00"
        conn = connect.connect()

        err_code = connect.book(conn, reh)
        conn.close()

        self.assertEqual(err_code, 1)

    def test_book_past(self):
        reh = connect.Rehearsal()
        reh.musician_id = 4
        reh.room_id = 1
        reh.date = "2022-10-01 12:00:00"
        conn = connect.connect()

        err_code = connect.book(conn, reh)
        conn.close()

        self.assertEqual(err_code, 2)

    def test_cancel(self):
        reh_id = 1001
        conn = connect.connect()

        err_code = connect.cancel(conn, reh_id)
        conn.close()

        self.assertEqual(err_code, 0)

    def test_get_rehs(self):
        acc_id = 37
        conn = connect.connect()
        reh_ids = [83, 450]

        res = connect.get_rehs(conn, acc_id)
        res = [res[0][0], res[1][0]]

        self.assertEqual(res, reh_ids)

    def test_rehs_by_base(self):
        base_id = 525
        conn = connect.connect()
        reh_ids = [542, 432]

        res = connect.rehs_by_base(conn, base_id)
        res_ids = [res[i][0] for i in range(len(res))]
        conn.close()

        self.assertEqual(len(res_ids), len(reh_ids))
        for i in range(len(res_ids)):
            self.assertIn(res_ids[i], reh_ids)

    def test_rehs_by_date(self):
        date = "2022-12-28 02:00:00"
        conn = connect.connect()
        reh_ids = [163]

        res = connect.rehs_by_date(conn, date)
        res_ids = [res[i][0] for i in range(len(res))]
        conn.close()

        self.assertEqual(len(res_ids), len(reh_ids))
        for i in range(len(res_ids)):
            self.assertIn(res_ids[i], reh_ids)

    def test_reh_info(self):
        reh_id = 1000
        conn = connect.connect()
        reh = [(datetime(2021, 12, 15, 22, 0), "rnhsp", "drum", 31, 969, "plxet",
               "tszefrbzmo", "+7-944-806-75-66", "esglaohrp@gmail.com")]

        res = connect.reh_info(conn, reh_id)
        conn.close()

        self.assertEqual(res, reh)


if __name__ == '__main__':
    unittest.main()
