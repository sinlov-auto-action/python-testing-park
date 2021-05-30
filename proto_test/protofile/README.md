## download protobuf utils

[https://github.com/protocolbuffers/protobuf/releases](https://github.com/protocolbuffers/protobuf/releases)

## 常用规字段说明

```
字段描述符:
package         包名      //package tutorial;
message         定义消息
required        字段必须
optional        字段可选
enum            枚举
repeated        字段可重复(会被定义成类似数组或list一类的结构)
syntax          指定.proto的风格  //syntax = "proto3"
service         rpc服务,不在此次学习范围内

数据类型:
bool
int32
uint32
uint64
sint32      使用变长编码，这些编码在负值时比int32高效的多
sint64      使用变长编码，有符号的整型值。编码时比通常的int64高效。
float
double
string
map<key_type, value_type> 
```

## 枚举

```protobuf
enum EnumAllowingAlias {
    option allow_alias = true;      //允许枚举值重复
    UNKNOWN = 0;
    STARTED = 1;
    RUNNING = 1;
}
```