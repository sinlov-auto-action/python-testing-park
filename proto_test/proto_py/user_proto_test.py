import unittest
from faker import Faker
import proto_test.proto_py.User_pb2 as User
import proto_test.proto_py.PhoneNumber_pb2 as PhoneNumber
import uuid
from google.protobuf import json_format
import json


class UserProtoPyTest(unittest.TestCase):

    def test_user_pb_serialization(self):
        fake = Faker()
        fake_name = fake.name()
        fake_email = fake.email()
        fake_phone_number = fake.phone_number()

        user_pb = User.User()
        user_pb.uid = str(uuid.uuid4())
        user_pb.name = fake_name
        user_pb.email = fake_email
        user_pb.age = 16
        user_pb.phoneNumber.number = fake_phone_number
        user_pb.phoneNumber.type = PhoneNumber.MOBILE
        print('user_pb %s' % user_pb)
        print('user_pb to json\n%s' % json_format.MessageToJson(user_pb))

        json_data = json.loads(json_format.MessageToJson(user_pb))

        self.assertEqual(json_data['age'], user_pb.age)
        self.assertEqual(json_data['name'], fake_name)
        self.assertEqual(json_data['email'], fake_email)
        self.assertEqual(json_data['phoneNumber']['number'], fake_phone_number)
        self.assertNotEqual(json_data['phoneNumber']['type'], PhoneNumber.MOBILE)
        self.assertEqual(json_data['phoneNumber']['type'], PhoneNumber.PhoneType.Name(PhoneNumber.MOBILE))

    def test_user_pb_deserialization(self):
        fake = Faker()
        fake_name = fake.name()
        fake_email = fake.email()
        fake_phone_number = fake.phone_number()

        user_pb = User.User()
        user_pb.uid = str(uuid.uuid4())
        user_pb.name = fake_name
        user_pb.email = fake_email
        user_pb.age = 16
        user_pb.phoneNumber.number = fake_phone_number
        user_pb.phoneNumber.type = PhoneNumber.HOME

        pb_serialize_user = user_pb.SerializeToString()
        print('user_pb.SerializeToString:\n{0}'.format(pb_serialize_user))

        user_ds = User.User()
        user_ds.ParseFromString(pb_serialize_user)
        self.assertEqual(user_ds.name, fake_name)
        self.assertEqual(user_ds.email, fake_email)
        self.assertEqual(user_ds.phoneNumber.number, fake_phone_number)
        self.assertEqual(user_ds.phoneNumber.type, PhoneNumber.HOME)
        pass


if __name__ == '__main__':
    unittest.main()
