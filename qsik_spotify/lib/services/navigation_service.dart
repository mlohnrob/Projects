import 'package:flutter/material.dart';

class NavigationService {
  GlobalKey<NavigatorState> _navigatonKey = GlobalKey<NavigatorState>();
  GlobalKey<NavigatorState> get navigationkey => _navigatonKey;

  bool pop() {
    return _navigatonKey.currentState.pop();
  }

  Future<dynamic> navigateTo(String routeName, {dynamic arguments}) {
    return _navigatonKey.currentState.pushNamed(routeName, arguments: arguments);
  }
}
