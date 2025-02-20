# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.image import image_service
from openstack import resource
from openstack import utils


class Image(resource.Resource):
    resources_key = 'images'
    base_path = '/images'
    service = image_service.ImageService()

    # capabilities
    allow_create = True
    allow_retrieve = True
    allow_update = True
    allow_delete = True
    allow_list = True
    patch_update = True

    # The image data (bytes or a file-like object)
    data = None
    # URI for the image
    location = resource.header("location")
    # Properties
    #: Hash of the image data used. The Image service uses this value
    #: for verification.
    checksum = resource.prop('checksum')
    #: The container format refers to whether the VM image is in a file
    #: format that also contains metadata about the actual VM.
    #: Container formats include OVF and Amazon AMI. In addition,
    #: a VM image might not have a container format - instead,
    #: the image is just a blob of unstructured data.
    container_format = resource.prop('container_format')
    #: The date and time when the image was created.
    created_at = resource.prop('created_at')
    #: Valid values are: aki, ari, ami, raw, iso, vhd, vdi, qcow2, or vmdk.
    #: The disk format of a VM image is the format of the underlying
    #: disk image. Virtual appliance vendors have different formats
    #: for laying out the information contained in a VM disk image.
    disk_format = resource.prop('disk_format')
    #: The minimum disk size in GB that is required to boot the image.
    min_disk = resource.prop('min_disk')
    #: The name of the image.
    name = resource.prop('name')
    #: The ID of the owner, or tenant, of the image.
    owner = resource.prop('owner')
    #: Properties, if any, that are associated with the image.
    properties = resource.prop('properties')
    #: Defines whether the image can be deleted.
    protected = resource.prop('protected', type=bool)
    #: The size of the image data, in bytes.
    size = resource.prop('size', type=int)
    #: When present, Glance will attempt to store the disk image data in the
    #: backing store indicated by the value of the header. When not present,
    #: Glance will store the disk image data in the backing store that is
    #: marked default. Valid values are: file, s3, rbd, swift, cinder,
    #: gridfs, sheepdog, or vsphere.
    store = resource.prop('store')
    #: The image status.
    status = resource.prop('status')
    #: Tags, if any, that are associated with the image.
    tags = resource.prop('tags')
    #: The date and time when the image was updated.
    updated_at = resource.prop('updated_at')
    #: The virtual size of the image.
    virtual_size = resource.prop('virtual_size')
    #: The image visibility.
    visibility = resource.prop('visibility')

    def upload_image(self, session):
        url = utils.urljoin(self._get_url(resource_id=self.id), 'file')

        headers = self.get_headers()
        headers['Content-Type'] = 'application/octet-stream'

        session.put(url, service=self.service, data=self.data, accept=None,
                    headers=headers)
