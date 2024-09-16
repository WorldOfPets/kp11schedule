--
-- ���� ������������ � ������� SQLiteStudio v3.4.4 � �� ��� 16 18:40:44 2024
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: cabinets
CREATE TABLE IF NOT EXISTS cabinets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL UNIQUE,
            type text
        );
INSERT INTO cabinets (id, name, type) VALUES (2, '402', NULL);
INSERT INTO cabinets (id, name, type) VALUES (3, '403', NULL);
INSERT INTO cabinets (id, name, type) VALUES (4, '404', NULL);
INSERT INTO cabinets (id, name, type) VALUES (5, '405', NULL);
INSERT INTO cabinets (id, name, type) VALUES (6, '406', NULL);
INSERT INTO cabinets (id, name, type) VALUES (7, '407', NULL);
INSERT INTO cabinets (id, name, type) VALUES (8, '408', NULL);
INSERT INTO cabinets (id, name, type) VALUES (13, '302', NULL);
INSERT INTO cabinets (id, name, type) VALUES (14, '303', NULL);
INSERT INTO cabinets (id, name, type) VALUES (15, '304', NULL);
INSERT INTO cabinets (id, name, type) VALUES (16, '305', NULL);
INSERT INTO cabinets (id, name, type) VALUES (17, '306', NULL);
INSERT INTO cabinets (id, name, type) VALUES (18, '310', NULL);
INSERT INTO cabinets (id, name, type) VALUES (19, '312', NULL);
INSERT INTO cabinets (id, name, type) VALUES (20, '200', NULL);
INSERT INTO cabinets (id, name, type) VALUES (21, '202', NULL);
INSERT INTO cabinets (id, name, type) VALUES (22, '203', NULL);
INSERT INTO cabinets (id, name, type) VALUES (23, '204', NULL);
INSERT INTO cabinets (id, name, type) VALUES (24, '205', NULL);
INSERT INTO cabinets (id, name, type) VALUES (25, '206', NULL);
INSERT INTO cabinets (id, name, type) VALUES (26, '209', NULL);
INSERT INTO cabinets (id, name, type) VALUES (27, '211', NULL);
INSERT INTO cabinets (id, name, type) VALUES (28, '212', NULL);
INSERT INTO cabinets (id, name, type) VALUES (29, '114�', NULL);
INSERT INTO cabinets (id, name, type) VALUES (30, '100', NULL);
INSERT INTO cabinets (id, name, type) VALUES (31, '114', NULL);
INSERT INTO cabinets (id, name, type) VALUES (32, '118', NULL);
INSERT INTO cabinets (id, name, type) VALUES (33, '119', NULL);
INSERT INTO cabinets (id, name, type) VALUES (34, '305�', NULL);

-- �������: groups
CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL UNIQUE,
            curator text
        );
INSERT INTO groups (id, name, curator) VALUES (1, '����-27 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (2, '�-25 (11��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (3, '����-22 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (4, '����-33 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (5, '����-32 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (6, '�-32 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (7, '����-42 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (8, '����-11 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (9, '����-13 (11 ��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (10, '����-14� (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (11, '����-11 (9 ��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (12, '�-24 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (13, '����-41 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (14, '�-12 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (15, '����-12 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (16, '����-35 (11��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (17, '�-11 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (18, '����-26 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (19, '����-31 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (20, '�-33 (11��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (21, '����-12 (9 ��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (22, '�-41 (9��)', NULL);
INSERT INTO groups (id, name, curator) VALUES (23, '����-28 (11��)', NULL);

-- �������: lesson
CREATE TABLE IF NOT EXISTS lesson (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL UNIQUE
        );
INSERT INTO lesson (id, name) VALUES (2, '������������ ������� � �����');
INSERT INTO lesson (id, name) VALUES (4, '��������-����� ');
INSERT INTO lesson (id, name) VALUES (7, '������������� ���������� ��������� � �������� ��������');
INSERT INTO lesson (id, name) VALUES (8, '�����������');
INSERT INTO lesson (id, name) VALUES (9, '���������� � ����������������� ������ ��������� ������� ������ (BigData)');
INSERT INTO lesson (id, name) VALUES (10, '�������� ����������� ���������������� ������������ ');
INSERT INTO lesson (id, name) VALUES (11, '������������ �������������� ������ ');
INSERT INTO lesson (id, name) VALUES (13, '�������������� ���������� ');
INSERT INTO lesson (id, name) VALUES (14, '������ ������-��������');
INSERT INTO lesson (id, name) VALUES (15, '���������� ���������� ������������ �����������');
INSERT INTO lesson (id, name) VALUES (16, '���������� ��������� ');
INSERT INTO lesson (id, name) VALUES (17, '������ �������������� �������');
INSERT INTO lesson (id, name) VALUES (18, '������������� � ������ ������������ ����������� ');
INSERT INTO lesson (id, name) VALUES (19, '������������ ���� ');
INSERT INTO lesson (id, name) VALUES (20, '������ ������������ �� ������������ ');
INSERT INTO lesson (id, name) VALUES (21, '��������� ���������� � ���������� � ������������� ������������ ����������� ');
INSERT INTO lesson (id, name) VALUES (22, '������ ���������� ���-����������');
INSERT INTO lesson (id, name) VALUES (23, '���������� ');
INSERT INTO lesson (id, name) VALUES (25, '���������� �������� � ��� ');
INSERT INTO lesson (id, name) VALUES (26, '������ ��������� ');
INSERT INTO lesson (id, name) VALUES (27, '���������� ��������');
INSERT INTO lesson (id, name) VALUES (28, '���������-����������� ��������� ������������� �������������� ������ ');
INSERT INTO lesson (id, name) VALUES (29, '���������� ������������ �������');
INSERT INTO lesson (id, name) VALUES (30, '����������� ���������� �������');
INSERT INTO lesson (id, name) VALUES (32, '�������������� �������� ��������� ');
INSERT INTO lesson (id, name) VALUES (35, '�������������� � ���������� ����������� ������������');
INSERT INTO lesson (id, name) VALUES (36, '������� ');
INSERT INTO lesson (id, name) VALUES (37, '�������������� ������� ��������� ���������� ');
INSERT INTO lesson (id, name) VALUES (39, '����������� ����');
INSERT INTO lesson (id, name) VALUES (40, '��������� ������� ');
INSERT INTO lesson (id, name) VALUES (41, '����������������� �������');
INSERT INTO lesson (id, name) VALUES (43, '������  ���������� ��� - ����������');
INSERT INTO lesson (id, name) VALUES (48, '������ ������������ � �������������� ���������� ');
INSERT INTO lesson (id, name) VALUES (52, '����������� ������������ ���-���������� ');
INSERT INTO lesson (id, name) VALUES (57, '����������� ������ � ����������� ');
INSERT INTO lesson (id, name) VALUES (58, '������ �������������� �������� ������� ');
INSERT INTO lesson (id, name) VALUES (59, '�������� �������������� ������ ');
INSERT INTO lesson (id, name) VALUES (61, '�������� ������������ ');
INSERT INTO lesson (id, name) VALUES (67, '���������� ���������� ');
INSERT INTO lesson (id, name) VALUES (68, '���������� ����������� ');
INSERT INTO lesson (id, name) VALUES (69, '��������� ������ ');
INSERT INTO lesson (id, name) VALUES (75, '������ �������������� � ����������� ������� ');
INSERT INTO lesson (id, name) VALUES (76, '���������� � ���������������� ������������ ');
INSERT INTO lesson (id, name) VALUES (78, '������ �������');
INSERT INTO lesson (id, name) VALUES (82, '�������� ');
INSERT INTO lesson (id, name) VALUES (87, '����������� ����������� �������� ');
INSERT INTO lesson (id, name) VALUES (89, '���������������� ������� � ��������� ');
INSERT INTO lesson (id, name) VALUES (90, '�����������, �������� ���������� � ���������������� ������������ �����');
INSERT INTO lesson (id, name) VALUES (95, '�������� ������ ���������� ');
INSERT INTO lesson (id, name) VALUES (96, '���������� � ���������������� �������������� ������� ');
INSERT INTO lesson (id, name) VALUES (97, '���������� ���������� ����� �� ������� ���������������� ������������ ');
INSERT INTO lesson (id, name) VALUES (99, '�������������� ');
INSERT INTO lesson (id, name) VALUES (101, '��������� � ������');
INSERT INTO lesson (id, name) VALUES (102, '������������ ����������������� ');
INSERT INTO lesson (id, name) VALUES (105, '��������� � ���������������� ������������� ������������ ');
INSERT INTO lesson (id, name) VALUES (107, '������������ ���������� �� ���������� ���������� ����� �� ��������� ��������� "����������� � ������� �������� �������� �����������" ("�������� �������")');
INSERT INTO lesson (id, name) VALUES (109, '���������� ���� �������������� ������ ');
INSERT INTO lesson (id, name) VALUES (111, '������� �������� ');
INSERT INTO lesson (id, name) VALUES (112, '����������� ������������ � ������ ������������ ������ � ���������� ');
INSERT INTO lesson (id, name) VALUES (113, '����� ');
INSERT INTO lesson (id, name) VALUES (114, '���������� ���������� ��� �������� ��������� ');
INSERT INTO lesson (id, name) VALUES (115, '�������������� � ������ �������������� ������ ');
INSERT INTO lesson (id, name) VALUES (117, '������ �������������� � ����������������');
INSERT INTO lesson (id, name) VALUES (119, '������ �������������� ��� ������ ');
INSERT INTO lesson (id, name) VALUES (122, '���������� ����������� ������ �������� ������ ');
INSERT INTO lesson (id, name) VALUES (127, '�������������� ������');
INSERT INTO lesson (id, name) VALUES (129, '������ ');
INSERT INTO lesson (id, name) VALUES (130, '����������������� ������� ������������ ������ ');
INSERT INTO lesson (id, name) VALUES (131, '�������������� ������������ ');
INSERT INTO lesson (id, name) VALUES (133, '���������������� ����������������� ');
INSERT INTO lesson (id, name) VALUES (134, '����������� ����������������� ������������ ������');
INSERT INTO lesson (id, name) VALUES (140, '������������� ���������� ��������� � �����������');
INSERT INTO lesson (id, name) VALUES (141, '���������� ������� ');
INSERT INTO lesson (id, name) VALUES (142, '��������� ');
INSERT INTO lesson (id, name) VALUES (144, '�������������� ������ �������������� ');
INSERT INTO lesson (id, name) VALUES (145, '��������������, ������������ � ����������� ���������������� ');
INSERT INTO lesson (id, name) VALUES (147, '������������ ������������ ����� ');
INSERT INTO lesson (id, name) VALUES (149, '������� ���� ');
INSERT INTO lesson (id, name) VALUES (164, '���������� ����� �� ��������� �������� �������� ����������-�������������� � �������������� ����� (�������������� �������������� ������ �� ��������� 1�, �������������� ���������� ����� �������������� ������)');
INSERT INTO lesson (id, name) VALUES (167, '����������� ���-����������  ');
INSERT INTO lesson (id, name) VALUES (189, '����������  ');
INSERT INTO lesson (id, name) VALUES (203, '������������� ����������');
INSERT INTO lesson (id, name) VALUES (205, '����������, �������������� � ������������ ');
INSERT INTO lesson (id, name) VALUES (219, '������� ������������� � ���������������  ');
INSERT INTO lesson (id, name) VALUES (246, '������ ������������ � ������ ������ ');
INSERT INTO lesson (id, name) VALUES (247, '����������������� � ��������� ������������ ');
INSERT INTO lesson (id, name) VALUES (250, '���������� �������������� ���������� ');
INSERT INTO lesson (id, name) VALUES (266, '��������� �������������� ������');
INSERT INTO lesson (id, name) VALUES (305, '������������ �������� ������� �������������� ');
INSERT INTO lesson (id, name) VALUES (310, '���������� ��������� ���������� ');
INSERT INTO lesson (id, name) VALUES (312, '����������� ���� � ���������������� ������������');
INSERT INTO lesson (id, name) VALUES (313, '���������� ���������� � ���������� �������������� ������');
INSERT INTO lesson (id, name) VALUES (314, '����������������� �������������� ������ (�� ��������� 1�, Linux, Windows)');

-- �������: num
CREATE TABLE IF NOT EXISTS num (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL UNIQUE,
            timestart text,
            timeend text
        );
INSERT INTO num (id, name, timestart, timeend) VALUES (1, '1', '9:00', '9:45');
INSERT INTO num (id, name, timestart, timeend) VALUES (2, '2', '9:55', '10:40');
INSERT INTO num (id, name, timestart, timeend) VALUES (3, '3', '11:00', '11:45');
INSERT INTO num (id, name, timestart, timeend) VALUES (4, '4', '11:55', '12:40');
INSERT INTO num (id, name, timestart, timeend) VALUES (5, '5', '13:00', '13:45');
INSERT INTO num (id, name, timestart, timeend) VALUES (6, '6', '13:55', '14:40');
INSERT INTO num (id, name, timestart, timeend) VALUES (7, '7', '15:00', '15:45');
INSERT INTO num (id, name, timestart, timeend) VALUES (8, '8', '15:55', '16:40');
INSERT INTO num (id, name, timestart, timeend) VALUES (9, '9', '16:50', '17:35');
INSERT INTO num (id, name, timestart, timeend) VALUES (10, '10', '17:45', '18:30');

-- �������: teachers
CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio text UNIQUE
        );
INSERT INTO teachers (id, fio) VALUES (1, '������� �.�.');
INSERT INTO teachers (id, fio) VALUES (2, '��������� �.�.');
INSERT INTO teachers (id, fio) VALUES (3, '��������� �.�.');
INSERT INTO teachers (id, fio) VALUES (4, '���������� �.�.');
INSERT INTO teachers (id, fio) VALUES (5, '������������ �.�.');
INSERT INTO teachers (id, fio) VALUES (6, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (7, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (8, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (9, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (10, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (11, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (12, '������������ �.�.');
INSERT INTO teachers (id, fio) VALUES (13, '����� �.�.');
INSERT INTO teachers (id, fio) VALUES (14, '��������� �.�.');
INSERT INTO teachers (id, fio) VALUES (15, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (16, '������� �.�.');
INSERT INTO teachers (id, fio) VALUES (17, '������ �.�.');
INSERT INTO teachers (id, fio) VALUES (18, '������� �.�.');
INSERT INTO teachers (id, fio) VALUES (19, '���������� �.�.');
INSERT INTO teachers (id, fio) VALUES (20, '��������� �.�.');
INSERT INTO teachers (id, fio) VALUES (21, '���������� �.�.');
INSERT INTO teachers (id, fio) VALUES (23, '������ �.�.');
INSERT INTO teachers (id, fio) VALUES (24, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (25, '������ �.�.');
INSERT INTO teachers (id, fio) VALUES (26, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (27, '��������');
INSERT INTO teachers (id, fio) VALUES (28, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (29, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (30, '���������� �.�.');
INSERT INTO teachers (id, fio) VALUES (31, '������� �.�.');
INSERT INTO teachers (id, fio) VALUES (32, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (33, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (34, '���������� �.�.');
INSERT INTO teachers (id, fio) VALUES (35, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (36, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (37, '������� �.�.');
INSERT INTO teachers (id, fio) VALUES (38, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (39, '����� �.�.');
INSERT INTO teachers (id, fio) VALUES (40, '������� �.�.');
INSERT INTO teachers (id, fio) VALUES (41, '������ �.�.');
INSERT INTO teachers (id, fio) VALUES (42, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (43, '�������� �.�.');
INSERT INTO teachers (id, fio) VALUES (44, '������ �.�.');
INSERT INTO teachers (id, fio) VALUES (45, '����������� �.�.');
INSERT INTO teachers (id, fio) VALUES (46, '������� ������');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
