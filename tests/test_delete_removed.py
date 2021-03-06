from unittest import TestCase, main

from interface.remote_actions import S3Interface
from interface.helper import get_files_to_delete


class TestDeleteRemoved(TestCase):

    def test_should_delete_one_file(self):
        local_file = ['file1']
        remote_files = ['file1', 'file2']
        removed_files = get_files_to_delete(local_file, remote_files)
        self.assertEqual({'Objects': [{'Key': 'file2'}]}, removed_files)

    def test_should_delete_file_with_extension(self):
        local_file = ['file1.exe', 'files2.exe']
        remote_files = ['file1.exe', 'files2.exe', 'program 2231.exe']
        removed_files = get_files_to_delete(local_file, remote_files)
        self.assertEqual({'Objects': [{'Key': 'program 2231.exe'}]}, removed_files)

    def test_should_not_delete_any_file(self):
        local_file = ['file1.exe', 'files2.exe']
        remote_files = ['file1.exe', 'files2.exe']
        removed_files = get_files_to_delete(local_file, remote_files)
        self.assertEqual({'Objects': []}, removed_files)

    def test_should_not_delete_empty_list(self):
        local_file = []
        remote_files = []
        removed_files = get_files_to_delete(local_file, remote_files)
        self.assertEqual({'Objects': []}, removed_files)

    def test_should_not_get_error_with_none_types(self):
        local_file = None
        remote_files = None
        removed_files = get_files_to_delete(local_file, remote_files)
        self.assertEqual({'Objects': []}, removed_files)

    def test_should_not_get_error_with_set_type(self):
        local_file = {'test'}
        remote_file = {}
        removed_files = get_files_to_delete(local_file, remote_file)
        self.assertEqual({'Objects': []}, removed_files)

    def test_should_not_get_error_with_tuple_type(self):
        local_file = ('test',)
        remote_file = ()
        removed_files = get_files_to_delete(local_file, remote_file)
        self.assertEqual({'Objects': []}, removed_files)

    def test_should_not_get_error_between_different_iterables(self):
        local_file = ()
        remote_file = {'test'}
        removed_files = get_files_to_delete(local_file, remote_file)
        self.assertEqual({'Objects': [{'Key': 'test'}]}, removed_files)
