#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to turtle_patrol_interface__srv__Patrol_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Patrol_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub vel: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub omega: f32,

}



impl Default for Patrol_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Patrol_Request::default())
  }
}

impl rosidl_runtime_rs::Message for Patrol_Request {
  type RmwMsg = super::srv::rmw::Patrol_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        vel: msg.vel,
        omega: msg.omega,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      vel: msg.vel,
      omega: msg.omega,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      vel: msg.vel,
      omega: msg.omega,
    }
  }
}


// Corresponds to turtle_patrol_interface__srv__Patrol_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Patrol_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub cmd: geometry_msgs::msg::Twist,

}



impl Default for Patrol_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Patrol_Response::default())
  }
}

impl rosidl_runtime_rs::Message for Patrol_Response {
  type RmwMsg = super::srv::rmw::Patrol_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        cmd: geometry_msgs::msg::Twist::into_rmw_message(std::borrow::Cow::Owned(msg.cmd)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        cmd: geometry_msgs::msg::Twist::into_rmw_message(std::borrow::Cow::Borrowed(&msg.cmd)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      cmd: geometry_msgs::msg::Twist::from_rmw_message(msg.cmd),
    }
  }
}






#[link(name = "turtle_patrol_interface__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__turtle_patrol_interface__srv__Patrol() -> *const std::ffi::c_void;
}

// Corresponds to turtle_patrol_interface__srv__Patrol
#[allow(missing_docs, non_camel_case_types)]
pub struct Patrol;

impl rosidl_runtime_rs::Service for Patrol {
    type Request = Patrol_Request;
    type Response = Patrol_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__turtle_patrol_interface__srv__Patrol() }
    }
}


